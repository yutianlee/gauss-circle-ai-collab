"""Freeze round210 exactly once after verified209 closure."""
import hashlib,json,sys,time
from pathlib import Path
from datetime import datetime,timezone
root=Path.cwd();sys.path.insert(0,str(root))
from math_collab.campaigns import validate_campaign,prepare_campaign
from math_collab.proof_obligations import load_graph,validate_graph
cid='gc-signed-near-frequency-cancellation';base=Path('rounds/codex-managed')/cid
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def put(p,b):
 for i in range(5):
  try:Path(p).write_bytes(b);return
  except OSError:
   if i==4:raise
   time.sleep(.2)
def write(p,o):put(p,(json.dumps(o,indent=2,ensure_ascii=False)+'\n').encode())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
old=read('state/active_campaign.yml');assert old['round_index']==209 and old['status']=='complete'
prior=Path('rounds/codex-managed/gc-complete-signed-tenth-moment')
for p,h in read(prior/'controls/artifact_hashes.json').items():assert sha(p)==h,p
g=load_graph(Path('state/proof_obligations.yml'));assert not validate_graph(g,root=root)
h=sha('state/proof_obligations.yml');assert h==old['starting_graph_sha256']
strategy='strategy/round210_signed_near_frequency_attack.md';now=datetime.now(timezone.utc).isoformat()
for d in ['briefs','reports','candidates','reviews','controls']:(base/d).mkdir(parents=True,exist_ok=True)
common=['protocol.md','state/proof_obligations.yml','state/active_campaign.yml',strategy,
'strategy/gauss_circle_strategy_checkpoint_round208_2026-09-27.md',
'rounds/codex-managed/gc-full-proof-signed-arithmetic-review/controls/conductor_bandlimited_strategy.md',
prior.as_posix()+'/synthesis.md']
specs=[('signed_rational_bins','discovery','selected_context',
'Attack the complete actual signed rational near-frequency target through phase-preserving bins at scale1/X. Retain internal modulation, derivative energy, both arms, variable width and moving prefix; a zero-th bin sum alone is unsafe. Derive a legal transfer with all label-interval costs, then attempt a quantitative bound on its ACTUAL signed input. Use at most two mechanisms. No exact-diagonal optimization or transform alone counts as gain; no absolute individual near integrals. An estimate must retain every bin and prefix, or state the complete unproved residual with its cost. Stop after report.',
common+[prior.as_posix()+'/reports/signed_fifth_convolution.md',prior.as_posix()+'/reviews/independent_rational_tenth_review.md',
'rounds/codex-managed/gc-signed-rational-filter-attack/controls/conductor_rational_norm_ledger.md']),
('actual_shifted_correlations','discovery','selected_context',
'Attack the complete actual physical tenth-moment or pointwise milestone by differencing/dispersion with fixed r2 or r2-pi coefficients, retaining oscillatory shifted correlations and the displaced window. At most two serious mechanisms. Price the diagonal, shift cutoff, mean correlation and summatory-error variation; do not import an unweighted shifted-correlation theorem without paying its phase variation. Seek actual signed oscillatory cancellation; a generic transformed identity is not gain. Exact primary sources may be used if a specific theorem is needed, with full hypotheses/cost audit. No broad source sweep. Stop after report.',
common+[prior.as_posix()+'/reports/actual_tenth_high_values.md',prior.as_posix()+'/reviews/independent_high_values_review.md',
prior.as_posix()+'/controls/conductor_tenth_power_ledger.md','proofs/kernels/gc_complete_square_root_large_values_moment_bound.md']),
('blind_bin_transfer','blind_rederiver','statement_only','Independently derive, refute or repair the isolated packet assertions. Read no other context and no web. Stop after seven-section report.',
['protocol.md',base.as_posix()+'/briefs/blind_bin_transfer_statement.md'])]
controls=['actual_coefficients','complete_scales','signed_absolute_distinction','exact_nonpairing_relations','real_endpoints','all_costs_restored','full_quarter_scope','statement_only_control']
tasks=[]
for ident,role,mode,target,ctx in specs:
 t=dict(id=ident,role=role,access_mode=mode,status='pending',target=target,context_files=ctx,required_controls=controls,
 required_output=['Seven numbered protocol sections; exact dependencies and first unproved step.','Only assigned report may be written; no shared state or successor edits.'],report_path=base.as_posix()+'/reports/'+ident+'.md')
 if mode=='statement_only':t['excluded_context']=['Everything except protocol and isolated packet, including generated general brief and web.']
 tasks.append(t)
m=dict(schema_version=1,round_index=210,round_type='complete_signed_near_frequency_attack',campaign_id=cid,title='Signed rational bins and actual shifted correlations',status='active',max_concurrency=3,coordinator='Codex',starting_graph_sha256=h,generated_at=now,
resource_policy=dict(analytical_algebraic_minimum_percent=95,numerical_experimental_maximum_percent=5,planned_numerical_percent=0,budget='Three bounded reports, at most two substantive mechanisms each, then one same-round seam cycle; planned zero mathematical experiments.'),
target_obligations=['GC-target','M9-M1','M9-M2','GC-complete-square-root-large-values-moment-bound'],
frozen_target=dict(question='Can phase-preserving rational bin energy or actual oscillatory shifted correlations prove the complete signed near-frequency target or another complete pointwise gain?',reference_formula='|O10(N)|<<T^(473/65+epsilon)N^-1/2 for every dyadic T^(166/325)<N<T^(242/325), with complete exact part and errors paid.',quantities=['Equivalent actual M10(H_N)<<T^(83/65+epsilon)N^-1/2 with reviewed errors.','This milestone would imply102/325 only; full quarter and M1/M2 remain open.']),
completion_criteria=['Three seven-section reports, including isolated independent derivation.','Complete cost ledger; actual gain or rigorous scoped failure and missing estimate.','Independent review of substantive selected claims.','Validated State Patch and ledger closure before successor design.'],controls=controls,exit_labels=['complete_arithmetic_gain_candidate','scoped_actual_method_no_go','no_new_bound_precise_open_residual'],tasks=tasks,
review_seams=[dict(id='actual_power_scope',requirement='Complete tenth norm, actual shifted correlations, all phase-variation costs and complements.'),dict(id='signed_bin_transfer',requirement='Internal bin modulation, derivative norm, moving-prefix decomposition and paid total interval energy.')],previous_goal_turn_classification='progress_completed_validated209_actual_exact_near_separation_and_scoped_method_no_go',scheduled_review='Next mandatory broad strategy/current-literature review211.')
assert not validate_campaign(m,g,root=root)
write('state/active_campaign.yml',m)
write('state/next_round_plan.yml',dict(round_index=210,status='active',campaign_id=cid,starting_graph_sha256=h,predecessor_round=209,tasks=[t['id'] for t in tasks]))
lp=Path('state/round_ledger.yml');raw=lp.read_bytes();s=raw.decode();ledger=json.loads(s)
assert ledger['rounds'][-1]['round_index']==209 and ledger['rounds'][-1]['status']=='closed'
entry=dict(round_index=210,campaign_id=cid,type=m['round_type'],status='active',objective=m['frozen_target']['question'],tasks=[{k:t[k] for k in ['id','role','status']} for t in tasks],resource_policy=m['resource_policy'],starting_graph_sha256=h,exit_labels=m['exit_labels'],started_at=now)
eol='\r\n' if '\r\n' in s else '\n';marker=eol+'  ]'+eol+'}';head,tail=s.rsplit(marker,1)
new=head+','+eol+eol.join('    '+line for line in json.dumps(entry,indent=2).splitlines())+marker+tail
new=new.replace('"active_round": 209','"active_round": 210',1);ledger['active_round']=210;ledger['rounds'].append(entry);assert json.loads(new)==ledger
put(lp,new.encode())
matrix=read('state/validation_matrix.yml');matrix.update(campaign_id=cid,promotion_status='round_210_active_no_promotion',graph_sha256=h,decision_rule='Actual signed tenth moment open; no theorem accepted at launch.')
for t in tasks:matrix['gates'].append(dict(id='round210_'+t['id'],status='pending',artifact=t['report_path']))
matrix['gates'].append(dict(id='round210_conductor_reconciliation',status='pending',artifact=base.as_posix()+'/reviews/conductor_round210_reconciliation.md'))
write('state/validation_matrix.yml',matrix)
write(base/'controls/starting_state_hashes.json',{p:sha(p) for p in ['state/proof_obligations.yml','state/best_proof_draft.md','strategy/gauss_circle_strategy_review_2026-09-23.md']})
failure=Path('state/failure_ledger.md');oldbytes=failure.read_bytes();prepare_campaign(m,g,root=root,graph_path=root/'state/proof_obligations.yml')
put(failure,oldbytes+b'\n\n## Round210 barriers\n\nExact relations are already target-safe. Full signed bins require internal modulation and amplitude derivatives; moving prefixes cannot be differentiated for free. Unweighted shifted-correlation errors must pay phase variation. Retain both old tenth-moment terms and all complements. No positive majorant is a signed lower bound.\n')
write(base/'controls/frozen_artifact_hashes.json',{p.as_posix():sha(p) for p in [base/'plan.json',Path(strategy)]+sorted((base/'briefs').glob('*.md'))})
for t in m['tasks']:t['status']='running'
write('state/active_campaign.yml',m);assert not validate_campaign(m,g,root=root)
print('Round210 frozen;209 archive verified; three briefs ready; graph unchanged.')
