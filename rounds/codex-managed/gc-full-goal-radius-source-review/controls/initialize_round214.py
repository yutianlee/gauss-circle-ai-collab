"""Freeze round214 once, only after verifying the closed213 archive."""
import hashlib,json,sys,time
from pathlib import Path
from datetime import datetime,timezone
root=Path.cwd();sys.path.insert(0,str(root))
from math_collab.campaigns import validate_campaign,prepare_campaign
from math_collab.proof_obligations import load_graph,validate_graph
cid='gc-full-goal-radius-source-review';base=Path('rounds/codex-managed')/cid
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def put(p,b):
 for i in range(5):
  try:Path(p).write_bytes(b);return
  except OSError:
   if i==4:raise
   time.sleep(.2)
def write(p,o):put(p,(json.dumps(o,indent=2,ensure_ascii=False)+'\n').encode())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
old=read('state/active_campaign.yml');assert old['round_index']==213 and old['status']=='complete'
prior=Path('rounds/codex-managed/gc-complete-centered-arithmetic')
for p,h in read(prior/'controls/artifact_hashes.json').items():assert sha(p)==h,p
assert not (base/'plan.json').exists()
g=load_graph(Path('state/proof_obligations.yml'));assert len(g['proof_obligations'])==399 and not validate_graph(g,root=root)
h=sha('state/proof_obligations.yml');assert h==old['starting_graph_sha256']
strategy='strategy/round214_full_goal_source_review.md';now=datetime.now(timezone.utc).isoformat()
for d in ['briefs','reports','candidates','reviews','controls']:(base/d).mkdir(parents=True,exist_ok=True)
common=['protocol.md','state/proof_obligations.yml','state/active_campaign.yml',strategy,
'strategy/gauss_circle_strategy_review_2026-09-23.md',
'strategy/gauss_circle_strategy_checkpoint_round211_2026-09-28.md',prior.as_posix()+'/synthesis.md']
specs=[
('signed_radius_sources','source_auditor','selected_context',
'Review current primary arithmetic and spectral correlation theorems for the literal complete signed radius-energy input. Fully audit at most two promising theorem interfaces, retaining actual four/eight r2 factors, growing additive shifts, anisotropic lengths, complete shell norms, real kernel and all restored costs. Seek a complete consequence or first exact failed hypothesis, not another unestimated reformulation. Do not repeat known invalid fixed-shift finite-complexity or positive-kernel imports. No siblings or successor work. Write seven sections and stop.',
common+[prior.as_posix()+'/reports/centered_shell_dispersion.md','rounds/codex-managed/gc-complete-four-point-correlation/reports/four_point_local_arithmetic.md']),
('full_goal_harmonic_sources','source_auditor','selected_context',
'Review current primary Gauss-circle, harmonic, high-moment and large-value methods against the full whole-discrepancy goal. Audit at most two promising full theorem interfaces and compare full M1/M2/GAR and moment/wave routes. Check current benchmark and source status; do not repeat the named exponent-pair or bilinear failures unless a genuinely new input changes their full consequence. Restore actual r2 coefficient, scale, norm and reconstruction costs and recommend one complete quantitative direction. No siblings or successor work. Write seven sections and stop.',
common+['rounds/codex-managed/gc-full-proof-signed-arithmetic-review/reports/arithmetic_full_frontier.md','rounds/codex-managed/gc-full-source-method-review/reports/harmonic_pair_sources.md','proofs/kernels/gc_complete_square_root_large_values_moment_bound.md']),
('blind_radius_optimization','blind_rederiver','statement_only',
'Derive, optimize or refute the isolated complete radius-certificate packet. Read only protocol and packet; no web, graph, manifest, strategy or other files. Arithmetic input remains hypothetical. Seven sections and stop.',
['protocol.md',base.as_posix()+'/briefs/blind_radius_optimization_statement.md'])]
controls=['actual_four_point_coefficients','complete_shifts_overlap','local_global_discrepancy','density_hypotheses','real_endpoints','all_restored_powers','signed_absolute_distinction','full_quarter_scope','statement_only_control','source_versions_hypotheses','complete_frontier']
tasks=[]
for ident,role,mode,target,ctx in specs:
 t=dict(id=ident,role=role,access_mode=mode,status='pending',target=target,context_files=ctx,required_controls=controls,
 required_output=['Seven numbered protocol sections with exact hypotheses, derivation, first unproved step, controls, dependencies and state recommendation.','Write only the assigned report; no shared state, synthesis, blind/sibling report or successor edits.'],report_path=base.as_posix()+'/reports/'+ident+'.md')
 if mode=='statement_only':t['excluded_context']=['Everything except protocol and isolated packet; exclude generated general brief, graph, strategy, all prior reports, siblings and web.']
 tasks.append(t)
m=dict(schema_version=1,round_index=214,round_type='mandatory_full_goal_source_review',campaign_id=cid,title='Full-goal strategy and current primary sources after211--213',status='active',max_concurrency=3,coordinator='Codex',starting_graph_sha256=h,generated_at=now,
resource_policy=dict(analytical_algebraic_minimum_percent=95,numerical_experimental_maximum_percent=5,planned_numerical_percent=0,budget='Three bounded reports; at most two full theorem audits per source task; one same-round seam cycle; planned zero experiments.'),
target_obligations=['GC-target','M9-M1','M9-M2','GC-complete-square-root-large-values-moment-bound'],
frozen_target=dict(question='Which complete actual-coefficient route should follow211--213 after current primary-source audits and full power comparison, preserving the quarter goal?',reference_formula='P(X)<<X^(1/4+epsilon); compare the complete signed radius gate Q_j<<T^epsilon(sqrt(N)+Nq^(-3/2)) with original high moments and all M1/M2 alternatives.',quantities=['No free pointwise recovery from radius mean: the actual sqrt(q) bandwidth price and all tails remain.','Every fixed-b gain is only a milestone. Determine the optimized reach of the radius method and audit exact coefficient/norm/scale hypotheses of proposed imports.']),
completion_criteria=['Three bounded seven-section reports, including an isolated important derivation.','Current bounded primary-literature and full-frontier review, with exact hypotheses, complete costs and next objective.','Independent mathematical/source seams and conductor synthesis at final hashes.','Validated State Patch and ledger closure before successor design; no unsupported exponent or parent promotion.'],
controls=controls,exit_labels=['costed_full_goal_strategy_adjustment','new_complete_candidate_requires_validation'],tasks=tasks,
review_seams=[dict(id='optimized_radius_certificate',requirement='Complete shell fractions, free integer lengths, complementary caps, full-goal limits and certificate scope.'),dict(id='current_sources_full_goal',requirement='Primary versions, exact coefficients, norms and ranges; complete frontiers, net powers and a concrete next objective.')],
previous_goal_turn_classification='progress_completed_validated213_signed_radius_bridge_and_actual_centered_periodic_obstructions',scheduled_review='Mandatory review214 after211--213; next broad review217 after214--216.')
assert not validate_campaign(m,g,root=root)
write('state/active_campaign.yml',m)
write('state/next_round_plan.yml',dict(round_index=214,status='active',campaign_id=cid,starting_graph_sha256=h,predecessor_round=213,tasks=[t['id'] for t in tasks]))
lp=Path('state/round_ledger.yml');raw=lp.read_bytes();s=raw.decode();ledger=json.loads(s)
assert ledger['rounds'][-1]['round_index']==213 and ledger['rounds'][-1]['status']=='closed'
entry=dict(round_index=214,campaign_id=cid,type=m['round_type'],status='active',objective=m['frozen_target']['question'],tasks=[{k:t[k] for k in ['id','role','status']} for t in tasks],resource_policy=m['resource_policy'],starting_graph_sha256=h,exit_labels=m['exit_labels'],started_at=now)
eol='\r\n' if '\r\n' in s else '\n';marker=eol+'  ]'+eol+'}';head,tail=s.rsplit(marker,1)
new=head+','+eol+eol.join('    '+line for line in json.dumps(entry,indent=2).splitlines())+marker+tail
new=new.replace('"active_round": 213','"active_round": 214',1);ledger['active_round']=214;ledger['rounds'].append(entry);assert json.loads(new)==ledger
put(lp,new.encode())
matrix=read('state/validation_matrix.yml');matrix.update(campaign_id=cid,promotion_status='round_214_active_no_promotion',graph_sha256=h,decision_rule='Mandatory full-goal source and strategy review; no theorem accepted at launch.')
for t in tasks:matrix['gates'].append(dict(id='round214_'+t['id'],status='pending',artifact=t['report_path']))
matrix['gates'].append(dict(id='round214_conductor_reconciliation',status='pending',artifact=base.as_posix()+'/reviews/conductor_round214_reconciliation.md'))
write('state/validation_matrix.yml',matrix)
write(base/'controls/starting_state_hashes.json',{p:sha(p) for p in ['state/proof_obligations.yml','state/best_proof_draft.md','strategy/gauss_circle_strategy_review_2026-09-23.md']})
failure=Path('state/failure_ledger.md');oldbytes=failure.read_bytes();prepare_campaign(m,g,root=root,graph_path=root/'state/proof_obligations.yml')
put(failure,oldbytes+b'\n\n## Round214 barriers\n\nThe213 signed radius gate remains unproved; its full bandwidth and enlarged-window costs are mandatory. Scalar centering, absolute DD with exact model terms and low-period nonnegative-model L1 complements have scoped obstructions, not signed counterexamples. Do not repeat those closures. Full quarter, original high moments, all small-t M1 HARD, independent M1 SMOOTH, M2 TOP/BAL/UNBAL, endpoints and GAR complement remain open. Audit current primary sources and net powers before selecting another complete objective.\n')
write(base/'controls/frozen_artifact_hashes.json',{p.as_posix():sha(p) for p in [base/'plan.json',Path(strategy)]+sorted((base/'briefs').glob('*.md'))})
for t in m['tasks']:t['status']='running'
write('state/active_campaign.yml',m);assert not validate_campaign(m,g,root=root)
print('Round214 frozen once; closed213 archive verified; three briefs ready; graph399 unchanged.')
