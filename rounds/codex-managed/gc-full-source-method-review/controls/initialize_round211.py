"""Freeze the mandatory round211 review once, after verifying closed210."""
import hashlib,json,sys,time
from pathlib import Path
from datetime import datetime,timezone
root=Path.cwd();sys.path.insert(0,str(root))
from math_collab.campaigns import validate_campaign,prepare_campaign
from math_collab.proof_obligations import load_graph,validate_graph
cid='gc-full-source-method-review';base=Path('rounds/codex-managed')/cid
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def put(p,b):
 for i in range(5):
  try:Path(p).write_bytes(b);return
  except OSError:
   if i==4:raise
   time.sleep(.2)
def write(p,o):put(p,(json.dumps(o,indent=2,ensure_ascii=False)+'\n').encode())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
old=read('state/active_campaign.yml');assert old['round_index']==210 and old['status']=='complete'
prior=Path('rounds/codex-managed/gc-signed-near-frequency-cancellation')
for p,h in read(prior/'controls/artifact_hashes.json').items():assert sha(p)==h,p
g=load_graph(Path('state/proof_obligations.yml'));assert not validate_graph(g,root=root)
h=sha('state/proof_obligations.yml');assert h==old['starting_graph_sha256']
strategy='strategy/round211_full_source_strategy_review.md';now=datetime.now(timezone.utc).isoformat()
for d in ['briefs','reports','candidates','reviews','controls']:(base/d).mkdir(parents=True,exist_ok=True)
common=['protocol.md','state/proof_obligations.yml','state/active_campaign.yml',strategy,
'strategy/gauss_circle_strategy_review_2026-09-23.md',
'strategy/gauss_circle_strategy_checkpoint_round208_2026-09-27.md',prior.as_posix()+'/synthesis.md',
'rounds/codex-managed/gc-full-proof-signed-arithmetic-review/controls/conductor_bandlimited_strategy.md']
specs=[('harmonic_pair_sources','source_auditor','selected_context',
'Review current primary Gauss-circle/harmonic literature and at most two exact exponent-pair or square-root exponential-sum theorem interfaces. Compare the complete physical r2 block with actual divisor decomposition, not arbitrary-weight application. Audit the exact pair convention, A/K ranges, partial intervals, residue-four shifts, smooth derivatives, all complements and restored power. Current benchmark/withdrawal checks are bounded screens, not an exhaustive claim. Seek a quantitative complete gain or identify the first failed hypothesis/cost; do not repeat earlier decoupling identities. No sibling/blind files. Stop after report.',
common+['rounds/codex-managed/gc-full-proof-signed-arithmetic-review/reports/harmonic_current_sources.md','proofs/kernels/gc_complete_square_root_large_values_moment_bound.md']),
('bilinear_arithmetic_sources','source_auditor','selected_context',
'Review the full M1/M2/GAR frontier and current primary arithmetic methods. Fully audit at most two promising theorems on bilinear/monomial square-root sums, twisted divisor correlations or a literal spectral substitute for the actual physical r2 hyperbola source. Preserve the outer character when a two-variable theorem allows it. Produce exact variable-length, phase, mask, modulus, coefficient norm, derivative and outer-summation costs; no inherited Kloosterman saving transplanted without a dictionary. Prefer a fresh source-compatible interface over repeating the priced absolute Abel/CRT failures. A complete failed import must stop at its first obstruction. No sibling/blind files. Stop after report.',
common+['rounds/codex-managed/gc-full-proof-signed-arithmetic-review/reports/arithmetic_full_frontier.md',prior.as_posix()+'/reports/actual_shifted_correlations.md',prior.as_posix()+'/reports/signed_rational_bins.md']),
('blind_hyperbola_transfer','blind_rederiver','statement_only',
'Independently derive, refute or repair the isolated hyperbola packet. Read only protocol and packet, no web or other context. Stop after seven-section report.',
['protocol.md',base.as_posix()+'/briefs/blind_hyperbola_statement.md'])]
controls=['actual_coefficients','complete_scales','signed_absolute_distinction','real_endpoints','all_costs_restored','full_quarter_scope','source_versions_hypotheses','statement_only_control']
tasks=[]
for ident,role,mode,target,ctx in specs:
 t=dict(id=ident,role=role,access_mode=mode,status='pending',target=target,context_files=ctx,required_controls=controls,required_output=['Seven numbered protocol sections; exact dependencies and first unproved step.','Only assigned report may be written; no shared state, synthesis or successor edits.'],report_path=base.as_posix()+'/reports/'+ident+'.md')
 if mode=='statement_only':t['excluded_context']=['Everything except protocol and isolated packet, including generated general brief and web.']
 tasks.append(t)
m=dict(schema_version=1,round_index=211,round_type='mandatory_full_source_strategy_review',campaign_id=cid,title='Full-source strategy and primary literature after208--210',status='active',max_concurrency=3,coordinator='Codex',starting_graph_sha256=h,generated_at=now,
resource_policy=dict(analytical_algebraic_minimum_percent=95,numerical_experimental_maximum_percent=5,planned_numerical_percent=0,budget='Three bounded reports; at most two full theorem audits per source task; one same-round seam cycle; planned zero experiments.'),
target_obligations=['GC-target','M9-M1','M9-M2','GC-complete-square-root-large-values-moment-bound'],
frozen_target=dict(question='Which complete actual-coefficient estimate should be attacked after208--210, judged by current primary hypotheses and restored powers across the full proof frontier?',reference_formula='P(X)<<X^(1/4+epsilon); all M1/M2 parents remain open. The fixed tenth milestone alone is not the full goal.',quantities=['Original signed tenth gate remains T^(473/65+epsilon)N^-1/2 on the complete middle band.','Compare a literal physical hyperbola/exponent-pair or bilinear input with all established signed-moment and internal routes.']),
completion_criteria=['Three seven-section reports and an important statement-only derivation.','Current bounded primary-literature check with exact source versions, hypotheses and costs.','Conductor full-frontier comparison and complete next objective with paid complements and limits.','Independent mathematical/source seams, validated State Patch and ledger closure before successor design.'],controls=controls,exit_labels=['costed_strategy_adjustment','new_complete_candidate_requires_validation'],tasks=tasks,
review_seams=[dict(id='complete_hyperbola_transfer',requirement='Both actual divisor arms, pair convention, range, phase, amplitudes, masks, optimal cutoff and reconstruction.'),dict(id='source_and_full_goal',requirement='Primary source hypotheses, exact norms and complete next target; full quarter and M1/M2 scope.')],
previous_goal_turn_classification='progress_completed_validated210_scoped_actual_arithmetic_transfer_and_method_failures',scheduled_review='Mandatory211 after208--210; next mandatory review214 after211--213.')
assert not validate_campaign(m,g,root=root)
write('state/active_campaign.yml',m)
write('state/next_round_plan.yml',dict(round_index=211,status='active',campaign_id=cid,starting_graph_sha256=h,predecessor_round=210,tasks=[t['id'] for t in tasks]))
lp=Path('state/round_ledger.yml');raw=lp.read_bytes();s=raw.decode();ledger=json.loads(s)
assert ledger['rounds'][-1]['round_index']==210 and ledger['rounds'][-1]['status']=='closed'
entry=dict(round_index=211,campaign_id=cid,type=m['round_type'],status='active',objective=m['frozen_target']['question'],tasks=[{k:t[k] for k in ['id','role','status']} for t in tasks],resource_policy=m['resource_policy'],starting_graph_sha256=h,exit_labels=m['exit_labels'],started_at=now)
eol='\r\n' if '\r\n' in s else '\n';marker=eol+'  ]'+eol+'}';head,tail=s.rsplit(marker,1)
new=head+','+eol+eol.join('    '+line for line in json.dumps(entry,indent=2).splitlines())+marker+tail
new=new.replace('"active_round": 210','"active_round": 211',1);ledger['active_round']=211;ledger['rounds'].append(entry);assert json.loads(new)==ledger
put(lp,new.encode())
matrix=read('state/validation_matrix.yml');matrix.update(campaign_id=cid,promotion_status='round_211_active_no_promotion',graph_sha256=h,decision_rule='Mandatory full strategy/source review; no theorem accepted at launch.')
for t in tasks:matrix['gates'].append(dict(id='round211_'+t['id'],status='pending',artifact=t['report_path']))
matrix['gates'].append(dict(id='round211_conductor_reconciliation',status='pending',artifact=base.as_posix()+'/reviews/conductor_round211_reconciliation.md'))
write('state/validation_matrix.yml',matrix)
write(base/'controls/starting_state_hashes.json',{p:sha(p) for p in ['state/proof_obligations.yml','state/best_proof_draft.md','strategy/gauss_circle_strategy_review_2026-09-23.md']})
failure=Path('state/failure_ledger.md');oldbytes=failure.read_bytes();prepare_campaign(m,g,root=root,graph_path=root/'state/proof_obligations.yml')
put(failure,oldbytes+b'\n\n## Round211 barriers\n\nThe210 H^9 bin input only recovers a coarse bound. Positive Abel variation and outer-absolute CRT closures fail on actual arithmetic controls. Neither is a signed no-go. A physical divisor decomposition must retain both complete arms, residue-four costs and every reconstruction scale. No external exponential-sum theorem applies to r2 weights without its exact coefficient interface. Full quarter and all M1/M2 routes remain open.\n')
write(base/'controls/frozen_artifact_hashes.json',{p.as_posix():sha(p) for p in [base/'plan.json',Path(strategy)]+sorted((base/'briefs').glob('*.md'))})
for t in m['tasks']:t['status']='running'
write('state/active_campaign.yml',m);assert not validate_campaign(m,g,root=root)
print('Round211 frozen;210 archive verified; three task briefs ready; graph unchanged.')
