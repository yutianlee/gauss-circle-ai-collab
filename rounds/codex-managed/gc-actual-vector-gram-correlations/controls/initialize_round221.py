"""Freeze221 once from the verified closed220 state. Do not rerun."""
import hashlib,json,sys,time
from pathlib import Path
from datetime import datetime,timezone
root=Path.cwd();sys.path.insert(0,str(root))
from math_collab.campaigns import validate_campaign,prepare_campaign
from math_collab.proof_obligations import load_graph,validate_graph
cid='gc-actual-vector-gram-correlations';base=Path('rounds/codex-managed')/cid
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def put(p,b):
 for i in range(5):
  try:Path(p).write_bytes(b);return
  except OSError:
   if i==4:raise
   time.sleep(.2)
def write(p,o):put(p,(json.dumps(o,indent=2,ensure_ascii=False)+'\n').encode())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
old=read('state/active_campaign.yml');assert old['round_index']==220 and old['status']=='complete'
archive=read('rounds/codex-managed/gc-full-goal-arithmetic-source-review/controls/artifact_hashes.json');assert len(archive)==30
for p,h in archive.items():assert sha(p)==h,p
assert not (base/'plan.json').exists()
g=load_graph(Path('state/proof_obligations.yml'));assert len(g['proof_obligations'])==401 and not validate_graph(g,root=root)
h=sha('state/proof_obligations.yml');assert h==old['closing_assessment']['resulting_graph_sha256']
strategy='strategy/round221_actual_vector_gram_and_correlations.md';now=datetime.now(timezone.utc).isoformat()
for d in ['briefs','reports','candidates','reviews','controls']:(base/d).mkdir(parents=True,exist_ok=True)
common=['protocol.md','state/proof_obligations.yml','state/active_campaign.yml',strategy,
'strategy/gauss_circle_strategy_checkpoint_round220_2026-09-28.md',
'proofs/kernels/gc_complete_square_root_large_values_moment_bound.md',
'proofs/kernels/gc_complete_distinct_radical_moment_reduction.md',
'proofs/kernels/gc_distinct_radical_absolute_certificate_obstruction.md',
'rounds/codex-managed/gc-complete-signed-tenth-moment/reports/actual_tenth_high_values.md',
'rounds/codex-managed/gc-complete-signed-radical-kernel/synthesis.md',
'rounds/codex-managed/gc-full-goal-arithmetic-source-review/synthesis.md']
specs=[
('actual_anchored_gram_attack','discovery','selected_context',
'Attack the COMPLETE actual signed I12(T,floor(T^(2/5)))<=T^(29/25+epsilon), equivalently the full physical twelfth moment, through one serious direct high-value/Gram-chain mechanism retaining the fixed actual coefficient vector and radius anchor through the joint estimate. Pay the small-class/repeated-class removal using216. Do not repeat209 positive weighted Cauchy, discard the vector endpoints, or replace the target by an unestimated remainder. Explicitly derive and try to estimate a complete actual joint correlation, keeping all levels, real cosine signs, unequal blocks and tails. A coefficient norm or finite identity alone is not a gain. Return a complete quantitative improvement or a scoped failed certificate with exact cost/first gap and actual-versus-enlarged control. Seven sections, at most one serious mechanism, no experiments, no shared edits/sibling/successor; stop.',common+[
'rounds/codex-managed/gc-full-goal-arithmetic-source-review/reports/full_frontier_sources.md']),
('actual_shifted_correlations','discovery','selected_context',
'Attack the same COMPLETE actual signed I12 upper bound at29/25 through one serious arithmetic joint-correlation mechanism with actual r2 coefficients and sf(n)>floor(T^(2/5)). An exact pair-increment, divisor or lattice-determinant grouping is allowed, but derive all weights/multiplicities and keep every real sign pattern/unequal block. Attempt a signed estimate before norms. Do not assume a shifted-convolution asymptotic, remove the arithmetic mask as smooth, or repeat the218 absolute dual-tuple closure. Explicitly restore the full moment and compare with10beta; a main term plus unestimated remainder is not a gain. Seven sections, exact proof or precise failed certificate, controls, first gap, complete powers. At most one serious mechanism, zero experiments, no shared edits/sibling/successor; stop.',common),
('blind_anchored_gram','blind_rederiver','statement_only',
'Read only protocol and the isolated packet. Prove or refute the finite fixed-vector Gram-chain, bordered PSD, pseudoinverse and translation-control statements. Seven sections, explicit prior-history disclosure; no web, experiments, application or sibling context. Write only assigned report and stop.',
['protocol.md',base.as_posix()+'/briefs/blind_anchored_gram_statement.md'])]
controls=['actual_coefficients_and_mask','absolute_radius_anchor','all_real_signs','complete_levels_blocks_tails','no_unproved_source_import','fixed_vector_vs_operator','singular_and_finite_controls','full_exponent_restoration','statement_only_rederivation','full_goal_scope']
tasks=[]
for ident,role,mode,target,ctx in specs:
 t=dict(id=ident,role=role,access_mode=mode,status='pending',target=target,context_files=ctx,required_controls=controls,required_output=['Seven numbered protocol sections; exact complete bound or scoped failed certificate, proof, first gap, controls, exact dependencies and state effect.','Only assigned report. Stop; no next round or shared-state/synthesis edit.'],report_path=base.as_posix()+'/reports/'+ident+'.md')
 if mode=='statement_only':t['excluded_context']=['All files except protocol and isolated statement; prior-agent history must be disclosed.']
 tasks.append(t)
m=dict(schema_version=1,round_index=221,round_type='complete_actual_vector_correlation_attack',campaign_id=cid,title='Complete actual-vector Gram and shifted-correlation attack',status='active',max_concurrency=3,coordinator='Codex',starting_graph_sha256=h,generated_at=now,
resource_policy=dict(analytical_algebraic_minimum_percent=95,numerical_experimental_maximum_percent=5,planned_numerical_percent=0,budget='Two bounded one-mechanism analytic reports, one isolated finite report, one same-round review/repair cycle; zero planned mathematical experiments.'),
target_obligations=['GC-target','GC-complete-square-root-large-values-moment-bound','GC-complete-distinct-radical-twelfth-reduction'],
frozen_target=dict(question='Can an actual fixed-vector Gram-chain or joint arithmetic shifted-correlation estimate prove the complete signed twelfth target with all costs restored?',reference_formula='I12(T,floor(T^(2/5)))<=C_epsilon T^(29/25+epsilon), equivalent to the full physical twelfth milestone; full goal remains P(X)<<X^(1/4+epsilon).',quantities=['Actual rho,Psi,w,r2 and all ordered distinct large squarefree classes from216, with every harmonic and cosine sign.','Paid small-class head15/13 and repeated-class error8beta-1/5; current complete bound10beta.','Fixed coefficient vector retained through the joint correlation; difference-only operator norms and new notation are not gains.','All levels, unequal blocks, endpoints and infinite tails; unbounded fixed-order family and original parents remain open.']),
completion_criteria=['Two bounded complete-target attack reports and one isolated Gram-chain report.','Exact actual-vector/application bindings, independent final-hash seams and controls.','Complete restored improvement or exact failed-certificate costs, synthesis, mechanically valid State Patch and221 closure.'],controls=controls,
exit_labels=['complete_actual_correlation_gain_requires_validation','complete_actual_correlation_attempt_no_new_bound'],tasks=tasks,
review_seams=[dict(id='fixed_vector_chain',requirement='Exact finite identities, singular cases, actual binding and no implicit coefficient enlargement.'),dict(id='arithmetic_joint_correlation',requirement='Actual arithmetic coefficients, class masks, sign patterns, multiplicities and complete costs.'),dict(id='full_moment_restoration',requirement='All levels, blocks, tails and restored powers; fixed-order/full-quarter distinction.')],
previous_goal_turn_classification='progress_completed_reviewed_strategy_evidence_changes_next_action_no_complete_estimate_gain',scheduled_review='Next mandatory broad strategy/current-primary review223 after220--222.')
assert not validate_campaign(m,g,root=root)
write('state/active_campaign.yml',m);write('state/next_round_plan.yml',dict(round_index=221,status='active',campaign_id=cid,starting_graph_sha256=h,predecessor_round=220,tasks=[t['id'] for t in tasks]))
lp=Path('state/round_ledger.yml');s=lp.read_text(encoding='utf-8');ledger=json.loads(s)
assert ledger['rounds'][-1]['round_index']==220 and ledger['rounds'][-1]['status']=='closed'
entry=dict(round_index=221,campaign_id=cid,type=m['round_type'],status='active',objective=m['frozen_target']['question'],tasks=[{k:t[k] for k in ['id','role','status']} for t in tasks],resource_policy=m['resource_policy'],starting_graph_sha256=h,exit_labels=m['exit_labels'],started_at=now)
marker='\n  ]\n}';head,tail=s.rsplit(marker,1);new=head+',\n'+'\n'.join('    '+line for line in json.dumps(entry,indent=2).splitlines())+marker+tail
new=new.replace('"active_round": 220','"active_round": 221',1);ledger['active_round']=221;ledger['rounds'].append(entry);assert json.loads(new)==ledger;put(lp,new.encode())
matrix=read('state/validation_matrix.yml');matrix.update(campaign_id=cid,promotion_status='round_221_active_no_promotion',graph_sha256=h,decision_rule='Complete actual-vector correlation attempt; no new estimate accepted at launch.')
for t in tasks:matrix['gates'].append(dict(id='round221_'+t['id'],status='pending',artifact=t['report_path']))
matrix['gates'].append(dict(id='round221_conductor_reconciliation',status='pending',artifact=base.as_posix()+'/reviews/conductor_round221_reconciliation.md'));write('state/validation_matrix.yml',matrix)
write(base/'controls/starting_state_hashes.json',{p:sha(p) for p in ['state/proof_obligations.yml','state/best_proof_draft.md','strategy/gauss_circle_strategy_review_2026-09-23.md']})
failure=Path('state/failure_ledger.md');oldbytes=failure.read_bytes();prepare_campaign(m,g,root=root,graph_path=root/'state/proof_obligations.yml')
put(failure,oldbytes+b'\n\n## Round221 fixed-vector correlation barriers\n\nRounds204/209 already show that positive r2-weighted difference Gram norms retain the diagonal and lose the actual vector anchor. Round217 rules out termwise absolute distinct-frequency closure;218 pays no complete signed gain from joint transforms;220 source transfers and arbitrary-row certificates do not establish the actual target. Retain fixed-vector chain endpoints or prove a new actual joint arithmetic estimate, and restore the entire signed moment. No smaller unestimated complement is a success.\n')
write(base/'controls/frozen_artifact_hashes.json',{p.as_posix():sha(p) for p in [base/'plan.json',Path(strategy)]+sorted((base/'briefs').glob('*.md'))})
for t in m['tasks']:t['status']='running'
write('state/active_campaign.yml',m);assert not validate_campaign(m,g,root=root)
print('Round221 frozen; closed220 archive30 verified; graph401 unchanged; three bounded briefs ready.')
