"""Freeze the scheduled review, preserving accepted mathematics."""
import hashlib,json,sys
from pathlib import Path
from datetime import datetime,timezone
root=Path.cwd();sys.path.insert(0,str(root))
from math_collab.campaigns import validate_campaign,prepare_campaign
from math_collab.proof_obligations import load_graph,validate_graph
cid='gc-full-proof-signed-arithmetic-review';base=Path('rounds/codex-managed')/cid
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def write(p,o):Path(p).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
old=read('state/active_campaign.yml');assert old['round_index']==207 and old['status']=='complete'
prior=Path('rounds/codex-managed/gc-signed-rational-filter-attack')
for p,h in read(prior/'controls/artifact_hashes.json').items():assert sha(p)==h,p
g=load_graph(Path('state/proof_obligations.yml'));assert not validate_graph(g,root=root)
h=sha('state/proof_obligations.yml');assert h==old['starting_graph_sha256']
now=datetime.now(timezone.utc).isoformat();strategy='strategy/round208_full_proof_strategy_review.md'
for d in ['briefs','reports','candidates','reviews','controls']:(base/d).mkdir(parents=True,exist_ok=True)
common=['protocol.md','state/proof_obligations.yml','state/active_campaign.yml',strategy,
'strategy/gauss_circle_strategy_review_2026-09-23.md','strategy/gauss_circle_strategy_checkpoint_round205_2026-09-26.md',
str(prior/'synthesis.md').replace('\\','/'),'proofs/kernels/gc_complete_square_root_large_values_moment_bound.md']
specs=[('harmonic_current_sources','source_auditor','selected_context',
'Check current primary literature for Gauss-circle improvements, withdrawals and harmonic/large-values/decoupling methods. Compare actual signed high values with the complete existing distribution. Fully price at most two promising exact theorem interfaces (beyond mere names), retaining trace, coefficient norms, scales, exceptional peaks and reconstruction. Give a bounded corpus/search log, exact versions and URLs, distinguish metadata from verified theorem. Seek a new complete estimate or explain the first missing arithmetic inequality. Do not design or start a successor.',common),
('arithmetic_full_frontier','source_auditor','selected_context',
'Review actual rational total-frequency aggregation versus arithmetic/spectral/shifted-correlation approaches, and compare with open full M1/M2 parents. Refresh current primary sources including potentially relevant new developments. Fully audit at most two exact theorem interfaces with actual norms, all-moduli/prime-power restrictions, shift/width ranges, main terms, signed cancellation and restored powers. Read the permitted205 complete frontier, plus207 rational ledger; no new transform by itself is a gain. State which full-source objective is quantitatively justified and its first unproved estimate. Stop after report.',common+['rounds/codex-managed/gc-full-frontier-moment-strategy-review/reports/internal_arithmetic_routes.md',str(prior/'controls/conductor_rational_norm_ledger.md').replace('\\','/')]),
('blind_moment_hierarchy','blind_rederiver','statement_only','Independently prove or refute every assertion requested in the isolated statement packet; no other context. Stop after the seven-section report.',['protocol.md',f'{base.as_posix()}/briefs/blind_moment_hierarchy_statement.md'])]
controls=['full_quarter_scope','complete_ranges','actual_coefficients','signed_absolute_distinction','all_costs_restored','real_endpoints','source_versions_hypotheses','independent_hierarchy']
tasks=[]
for ident,role,mode,target,ctx in specs:
 t=dict(id=ident,role=role,access_mode=mode,status='pending',target=target,context_files=ctx,required_controls=controls,
 required_output=['Seven numbered protocol sections; exact citations and artifact dependencies.','Write only the assigned report; no shared state or successor edits.'],report_path=f'{base.as_posix()}/reports/{ident}.md')
 if mode=='statement_only':t['excluded_context']=['Everything except protocol and the isolated statement packet, including generated general brief and web.']
 tasks.append(t)
m=dict(schema_version=1,round_index=208,round_type='full_proof_strategy_current_literature_review',campaign_id=cid,title='Full-proof signed arithmetic strategy and current literature review',status='active',max_concurrency=3,coordinator='Codex',starting_graph_sha256=h,generated_at=now,
resource_policy=dict(analytical_algebraic_minimum_percent=100,numerical_experimental_maximum_percent=0,planned_numerical_percent=0,budget='Three bounded reports and one same-round seam cycle; at most two fully priced theorem interfaces per source task; no mathematical numerical experiments.'),
target_obligations=['GC-target','M9-M1','M9-M2','GC-complete-square-root-large-values-moment-bound'],
frozen_target=dict(question='Which complete actual signed arithmetic estimate should be pursued after205--207, with current primary-source costs and a route toward the full quarter theorem?',reference_formula='P(X)<<X^(1/4+epsilon); retain the open full M1/M2 frontier and sufficient arbitrarily-high-fixed-moment route.',quantities=['Current p12 milestone radius T^(29/25), only pointwise102/325.','Round207 termwise rational majorant>=X^3H is a scoped obstruction, not a signed lower bound.']),
completion_criteria=['Three seven-section reports and an important statement-only derivation.','Current bounded primary-literature check with exact source hypotheses and costs.','Conductor comparison and complete next objective with complements and full-proof limits.','Independent seams; validated State Patch and closed ledger before successor design.'],controls=controls,exit_labels=['costed_strategy_adjustment','new_complete_candidate_requires_validation'],tasks=tasks,
review_seams=[dict(id='all_moment_scope',requirement='Exact moment powers, endpoints, complements and full theorem.'),dict(id='source_selection',requirement='Primary hypotheses, restored costs and selection based on complete source.')],previous_goal_turn_classification='progress_completed_validated207_scoped_obstruction_changes_next_action',scheduled_review='This is mandatory208; next mandatory review211 after208--210.')
assert not validate_campaign(m,g,root=root)
write('state/active_campaign.yml',m)
write('state/next_round_plan.yml',dict(round_index=208,status='active',campaign_id=cid,starting_graph_sha256=h,predecessor_round=207,tasks=[t['id'] for t in tasks]))
lp=Path('state/round_ledger.yml');s=lp.read_bytes().decode('utf-8');ledger=json.loads(s)
assert ledger['rounds'][-1]['round_index']==207 and ledger['rounds'][-1]['status']=='closed'
entry=dict(round_index=208,campaign_id=cid,type=m['round_type'],status='active',objective=m['frozen_target']['question'],tasks=[{k:t[k] for k in ['id','role','status']} for t in tasks],resource_policy=m['resource_policy'],starting_graph_sha256=h,exit_labels=m['exit_labels'],started_at=now)
eol='\r\n' if '\r\n' in s else '\n';marker=eol+'  ]'+eol+'}';head,tail=s.rsplit(marker,1)
new=head+','+eol+eol.join('    '+line for line in json.dumps(entry,indent=2).splitlines())+marker+tail
new=new.replace('"active_round": 207','"active_round": 208',1);ledger['active_round']=208;ledger['rounds'].append(entry);assert json.loads(new)==ledger
lp.write_bytes(new.encode('utf-8'))
matrix=read('state/validation_matrix.yml');matrix.update(campaign_id=cid,promotion_status='round_208_active_no_promotion',graph_sha256=h,decision_rule='Strategy review; no theorem accepted at launch.')
for t in tasks:matrix['gates'].append(dict(id='round208_'+t['id'],status='pending',artifact=t['report_path']))
matrix['gates'].append(dict(id='round208_conductor_reconciliation',status='pending',artifact=f'{base.as_posix()}/reviews/conductor_round208_reconciliation.md'))
write('state/validation_matrix.yml',matrix)
write(base/'controls/starting_state_hashes.json',{p:sha(p) for p in ['state/proof_obligations.yml','state/best_proof_draft.md','strategy/gauss_circle_strategy_review_2026-09-23.md']})
failure=Path('state/failure_ledger.md');raw=failure.read_bytes();prepare_campaign(m,g,root=root,graph_path=root/'state/proof_obligations.yml')
failure.write_bytes(raw+b'\n\n## Round208 barriers\n\nThe207 obstruction concerns termwise absolute sextuple integrals, not the signed moment or cancellation after total-frequency aggregation. Current masks and variance are paid. Further isolated transforms and repeated recovered bounds are not gains. Full quarter scope requires arbitrarily high fixed moments or complete M1/M2 parents.\n')
write(base/'controls/frozen_artifact_hashes.json',{p.as_posix():sha(p) for p in [base/'plan.json',Path(strategy)]+sorted((base/'briefs').glob('*.md'))})
for t in m['tasks']:t['status']='running'
write('state/active_campaign.yml',m);assert not validate_campaign(m,g,root=root)
print('Round208 frozen;207 archive verified; graph unchanged; three task briefs ready.')
