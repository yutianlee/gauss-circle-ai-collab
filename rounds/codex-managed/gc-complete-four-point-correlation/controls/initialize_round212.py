"""Freeze round212 once, only after verifying the closed211 archive."""
import hashlib,json,sys,time
from pathlib import Path
from datetime import datetime,timezone
root=Path.cwd();sys.path.insert(0,str(root))
from math_collab.campaigns import validate_campaign,prepare_campaign
from math_collab.proof_obligations import load_graph,validate_graph
cid='gc-complete-four-point-correlation';base=Path('rounds/codex-managed')/cid
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def put(p,b):
 for i in range(5):
  try:Path(p).write_bytes(b);return
  except OSError:
   if i==4:raise
   time.sleep(.2)
def write(p,o):put(p,(json.dumps(o,indent=2,ensure_ascii=False)+'\n').encode())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
old=read('state/active_campaign.yml');assert old['round_index']==211 and old['status']=='complete'
prior=Path('rounds/codex-managed/gc-full-source-method-review')
for p,h in read(prior/'controls/artifact_hashes.json').items():assert sha(p)==h,p
assert not (base/'plan.json').exists()
g=load_graph(Path('state/proof_obligations.yml'));assert len(g['proof_obligations'])==399 and not validate_graph(g,root=root)
h=sha('state/proof_obligations.yml');assert h==old['starting_graph_sha256']
strategy='strategy/round212_complete_four_point_attack.md';now=datetime.now(timezone.utc).isoformat()
for d in ['briefs','reports','candidates','reviews','controls']:(base/d).mkdir(parents=True,exist_ok=True)
common=['protocol.md','state/proof_obligations.yml','state/active_campaign.yml',strategy,
'strategy/gauss_circle_strategy_checkpoint_round211_2026-09-28.md',
prior.as_posix()+'/controls/conductor_two_stage_strategy.md',prior.as_posix()+'/reviews/independent_two_stage_review.md']
specs=[
('four_point_local_arithmetic','discovery','selected_context',
'Attack a complete actual four-point r2 short-interval discrepancy input at ell=N/(1+Thk/N^(3/2)), uniformly in all shifts and real endpoints. Derive any mean or smooth density rather than presume it; retain repeated-shift and small-product behavior. Seek a quantitative local or averaged arithmetic error that truly improves the full A4 bound. At most one full primary theorem audit if useful; distinguish full-size convex-body averages from anisotropic short boxes and absolute shift averages. If an import fails, identify its first exact hypothesis or restored-cost obstruction. No sibling files or successor work. Stop after seven-section report.',common),
('four_point_oscillatory_attack','discovery','selected_context',
'Attack the complete oscillatory A4 directly on the actual r2 coefficients using exact divisor or Gaussian norm representations and cancellation inside the n-sum. First price small products and h=k under the actual divisor envelope, then retain the entire remaining domain. Try a genuinely signed shift-average or dispersion mechanism; give a complete quantitative inequality or precise actual-source obstruction. An exact transform alone is not success, and do not repeat the already failed outer-absolute CRT closure. No sibling files or successor work. Stop after seven-section report.',
common+['rounds/codex-managed/gc-signed-near-frequency-cancellation/reports/actual_shifted_correlations.md','rounds/codex-managed/gc-signed-near-frequency-cancellation/reviews/independent_shifted_correlations_review.md']),
('blind_local_interval_transfer','blind_rederiver','statement_only',
'Derive or refute the isolated local-discrepancy transfer and full power criterion; read only protocol and isolated packet, no web or other files. The arithmetic input is hypothetical. Stop after seven-section report.',
['protocol.md',base.as_posix()+'/briefs/blind_local_interval_statement.md'])]
controls=['actual_four_point_coefficients','complete_shifts_overlap','local_global_discrepancy','density_hypotheses','real_endpoints','all_restored_powers','signed_absolute_distinction','full_quarter_scope','statement_only_control']
tasks=[]
for ident,role,mode,target,ctx in specs:
 t=dict(id=ident,role=role,access_mode=mode,status='pending',target=target,context_files=ctx,required_controls=controls,
 required_output=['Seven numbered protocol sections with exact hypotheses, derivation, first unproved step, controls, dependencies and state recommendation.','Write only the assigned report; no shared state, synthesis, blind/sibling report or successor edits.'],report_path=base.as_posix()+'/reports/'+ident+'.md')
 if mode=='statement_only':t['excluded_context']=['Everything except protocol and isolated packet; exclude generated general brief, graph, strategy, all prior reports, siblings and web.']
 tasks.append(t)
m=dict(schema_version=1,round_index=212,round_type='complete_actual_four_point_attack',campaign_id=cid,title='Complete actual four-point oscillatory correlation attack',status='active',max_concurrency=3,coordinator='Codex',starting_graph_sha256=h,generated_at=now,
resource_policy=dict(analytical_algebraic_minimum_percent=95,numerical_experimental_maximum_percent=5,planned_numerical_percent=0,budget='Three bounded reports; at most one full primary theorem audit in the local-arithmetic task; one same-round seam cycle; planned zero experiments.'),
target_obligations=['GC-target','M9-M1','M9-M2','GC-complete-square-root-large-values-moment-bound'],
frozen_target=dict(question='Can the complete actual four-point shift average satisfy the selected power, or what exact arithmetic input or scoped obstruction remains after all costs?',reference_formula='sup_R (LK)^(-1)sum_(h<L,k<K)|D_(h,k)(R)| << T^(166/325+epsilon), with the actual r2 product and every T^(166/325)<N<T^(242/325).',quantities=['L=max(2,ceil(N^(1/2)T^(-83/325))); K=max(2,ceil(NT^(-166/325))); zero-extended full four-point D; modulus only after full n-sum.','All h=k and small shift products retained until paid. The102/325 consequence is a milestone, not the full quarter goal.']),
completion_criteria=['Three bounded seven-section reports, including an isolated important derivation.','A complete quantitative bound or exact remaining arithmetic hypothesis with every sector and cost retained.','Independent mathematical/source seams and conductor synthesis at final hashes.','Validated State Patch and ledger closure before successor design; no unsupported exponent or parent promotion.'],
controls=controls,exit_labels=['complete_four_point_gain_requires_validation','essential_local_transfer_actual_input_open','scoped_actual_four_point_obstruction'],tasks=tasks,
review_seams=[dict(id='complete_actual_arithmetic',requirement='Exact r2 coefficients, density/source uniformity, complete shifts and true modulus placement.'),dict(id='local_transfer_and_complete_power',requirement='All local endpoints, boundary terms, main terms, powers, full band and reconstruction.')],
previous_goal_turn_classification='progress_completed_validated211_costed_source_review_and_complete_four_point_interface',scheduled_review='Next mandatory broad strategy/current-primary-source review214 after211--213.')
assert not validate_campaign(m,g,root=root)
write('state/active_campaign.yml',m)
write('state/next_round_plan.yml',dict(round_index=212,status='active',campaign_id=cid,starting_graph_sha256=h,predecessor_round=211,tasks=[t['id'] for t in tasks]))
lp=Path('state/round_ledger.yml');raw=lp.read_bytes();s=raw.decode();ledger=json.loads(s)
assert ledger['rounds'][-1]['round_index']==211 and ledger['rounds'][-1]['status']=='closed'
entry=dict(round_index=212,campaign_id=cid,type=m['round_type'],status='active',objective=m['frozen_target']['question'],tasks=[{k:t[k] for k in ['id','role','status']} for t in tasks],resource_policy=m['resource_policy'],starting_graph_sha256=h,exit_labels=m['exit_labels'],started_at=now)
eol='\r\n' if '\r\n' in s else '\n';marker=eol+'  ]'+eol+'}';head,tail=s.rsplit(marker,1)
new=head+','+eol+eol.join('    '+line for line in json.dumps(entry,indent=2).splitlines())+marker+tail
new=new.replace('"active_round": 211','"active_round": 212',1);ledger['active_round']=212;ledger['rounds'].append(entry);assert json.loads(new)==ledger
put(lp,new.encode())
matrix=read('state/validation_matrix.yml');matrix.update(campaign_id=cid,promotion_status='round_212_active_no_promotion',graph_sha256=h,decision_rule='Complete actual four-point attack; finite reduction alone does not prove the arithmetic input.')
for t in tasks:matrix['gates'].append(dict(id='round212_'+t['id'],status='pending',artifact=t['report_path']))
matrix['gates'].append(dict(id='round212_conductor_reconciliation',status='pending',artifact=base.as_posix()+'/reviews/conductor_round212_reconciliation.md'))
write('state/validation_matrix.yml',matrix)
write(base/'controls/starting_state_hashes.json',{p:sha(p) for p in ['state/proof_obligations.yml','state/best_proof_draft.md','strategy/gauss_circle_strategy_review_2026-09-23.md']})
failure=Path('state/failure_ledger.md');oldbytes=failure.read_bytes();prepare_campaign(m,g,root=root,graph_path=root/'state/proof_obligations.yml')
put(failure,oldbytes+b'\n\n## Round212 barriers\n\nThe complete four-point target remains open. Global unweighted errors incur full phase variation; a local discrepancy input is stronger and must be proved. Every actual shift, repeated factor, small product, density and overlap must remain until its normalized cost is paid. No positive certificate floor is a signed arithmetic lower bound.211 scalar/bilinear imports and210 absolute closures are parked. Full quarter and all M1/M2 alternatives remain open.\n')
write(base/'controls/frozen_artifact_hashes.json',{p.as_posix():sha(p) for p in [base/'plan.json',Path(strategy)]+sorted((base/'briefs').glob('*.md'))})
for t in m['tasks']:t['status']='running'
write('state/active_campaign.yml',m);assert not validate_campaign(m,g,root=root)
print('Round212 frozen once; closed211 archive verified; three briefs ready; graph399 unchanged.')
