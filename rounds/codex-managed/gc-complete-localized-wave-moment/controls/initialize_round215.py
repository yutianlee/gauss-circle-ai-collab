"""Freeze round215 exactly once after verifying closed214."""
import hashlib,json,sys,time
from pathlib import Path
from datetime import datetime,timezone
root=Path.cwd();sys.path.insert(0,str(root))
from math_collab.campaigns import validate_campaign,prepare_campaign
from math_collab.proof_obligations import load_graph,validate_graph
cid='gc-complete-localized-wave-moment';base=Path('rounds/codex-managed')/cid
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def put(p,b):
 for i in range(5):
  try:Path(p).write_bytes(b);return
  except OSError:
   if i==4:raise
   time.sleep(.2)
def write(p,o):put(p,(json.dumps(o,indent=2,ensure_ascii=False)+'\n').encode())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
old=read('state/active_campaign.yml');assert old['round_index']==214 and old['status']=='complete'
prior=Path('rounds/codex-managed/gc-full-goal-radius-source-review')
archive=read(prior/'controls/artifact_hashes.json');assert len(archive)==26
for p,h in archive.items():assert sha(p)==h,p
assert not (base/'plan.json').exists()
g=load_graph(Path('state/proof_obligations.yml'));assert len(g['proof_obligations'])==399 and not validate_graph(g,root=root)
h=sha('state/proof_obligations.yml');assert h==old['starting_graph_sha256']
strategy='strategy/round215_complete_localized_wave_attack.md';now=datetime.now(timezone.utc).isoformat()
for d in ['briefs','reports','candidates','reviews','controls']:(base/d).mkdir(parents=True,exist_ok=True)
common=['protocol.md','state/proof_obligations.yml','state/active_campaign.yml',strategy,'strategy/gauss_circle_strategy_checkpoint_round214_2026-09-28.md',prior.as_posix()+'/reports/full_goal_harmonic_sources.md',prior.as_posix()+'/reviews/independent_harmonic_sources_review.md']
specs=[
('weighted_envelope_transfer','discovery','selected_context',
'Derive and quantitatively test a legal amplitude-dependent cone-envelope bound for the complete frozen weighted tube moment. Inspect the primary Guth--Maldague amplitude-dependent theorem and exact envelope definitions; at most this one source interface. Preserve the spatial weight, thresholds, all packets, actual modulated coefficients, localization/window/tail costs and narrow/aligned directions. Prove the strongest complete justified inequality or a precisely scoped analytic/source obstruction. Do not repeat the already priced generic Theorem3 small-cap calculation. No siblings or successor work. Seven sections and stop.',common),
('actual_lattice_envelopes','discovery','selected_context',
'Analytically attack the complete C215 moment on its actual lattice coefficients, retaining the common center modulation, every direction/norm/window and all tails. Seek an actual coefficient-sensitive envelope or arithmetic bound with a complete power gain; transformations must retain their full remainder and cost. At most one promising primary-source import, fully audited. If no gain, give the first precise open step and any rigorously proved complete certificate limitation, never an arbitrary-array control labeled as an actual obstruction. No siblings or successor work. Seven sections and stop.',common+['proofs/kernels/gc_complete_square_root_large_values_moment_bound.md']),
('blind_spatial_kernel','blind_rederiver','statement_only',
'Independently derive the isolated spatial-weight/kernel packet, compare both orders of taking absolute values, and retain certificate versus actual signed scope. Read only protocol and isolated packet; no web or other context. Seven sections and stop.',
['protocol.md',base.as_posix()+'/briefs/blind_spatial_kernel_statement.md'])]
controls=['exact_r2_lift','actual_common_modulation','weighted_fourier_normalization','all_windows_tails','narrow_aligned_directions','complete_coefficient_norms','source_hypotheses','all_restored_powers','actual_arbitrary_distinction','certificate_signed_distinction','real_endpoints','full_quarter_scope','statement_only_control']
tasks=[]
for ident,role,mode,target,ctx in specs:
 t=dict(id=ident,role=role,access_mode=mode,status='pending',target=target,context_files=ctx,required_controls=controls,required_output=['Seven numbered protocol sections with exact hypotheses, derivation, first unproved step, controls, dependencies and state recommendation.','Write only assigned report; no shared state, synthesis, blind/sibling report or successor edits.'],report_path=base.as_posix()+'/reports/'+ident+'.md')
 if mode=='statement_only':t['excluded_context']=['Everything except protocol and isolated packet; exclude generated general brief, graph, manifest, strategy, all prior/current reports and web.']
 tasks.append(t)
m=dict(schema_version=1,round_index=215,round_type='complete_actual_localized_wave_attack',campaign_id=cid,title='Complete actual weighted lattice-wave tenth moment',status='active',max_concurrency=3,coordinator='Codex',starting_graph_sha256=h,generated_at=now,
resource_policy=dict(analytical_algebraic_minimum_percent=95,numerical_experimental_maximum_percent=5,planned_numerical_percent=0,budget='Three bounded reports; one primary amplitude-envelope interface and at most one arithmetic import; one same-round seam cycle; zero planned experiments.'),
target_obligations=['GC-target','GC-complete-square-root-large-values-moment-bound','M9-M1','M9-M2'],
frozen_target=dict(question='Prove or rigorously delimit the complete actual weighted localized cone-wave moment(C215), retaining its full-quarter extension criterion.',reference_formula='C(T,N)=sum_j integral W(y)|phi(y/N)eta(u/N)F_N(y/sqrt(N),R_j+u/sqrt(N))|^10 dydu << T^(83/65+epsilon), for every T^(166/325)<N<T^(242/325).',quantities=['Exact c_m=|m|^(-3/2)Psi(|m|/sqrt(T))v(|m|^2/N); every direction, norm, common center phase, radius window, real endpoint and Schwartz tail.','I=[T/sqrt(2),sqrt(3)T], J=ceil((sqrt(3)-1/sqrt(2))T/sqrt(N)), R_j=T/sqrt(2)+j sqrt(N),0<=j<=J; fixed product cutoff and W=C_A(1+|y|^2)^(-100).','C215 implies the complete tenth gate by fixed spatial bandwidth and du=sqrt(N)dR;102/325 is a milestone only. The full goal still requires a sufficient complete moment family or alternative parents.']),
completion_criteria=['Three bounded seven-section reports, including an isolated important kernel derivation.','Complete weighted analytic and actual arithmetic costs, with first unproved steps and genuine no-go scopes.','Independent final-hash seams and conductor synthesis preserving every full-goal alternative.','Validated State Patch and ledger closure before successor design; no unsupported moment/exponent/parent promotion.'],controls=controls,
exit_labels=['complete_localized_moment_candidate_requires_validation','complete_localized_moment_still_open'],tasks=tasks,
review_seams=[dict(id='weighted_analytic_transfer',requirement='Exact source envelope, weighted norm, thresholds, windows and tails with all restored powers.'),dict(id='actual_arithmetic_scope',requirement='Actual lattice coefficients, common modulation and complete signed or certificate estimates.'),dict(id='spatial_kernel_control',requirement='Exact Fourier factors, actual mass binding, both absolute-value orders and signed distinction.')],
previous_goal_turn_classification='progress_completed_validated214_full_goal_radius_limit_primary_source_review_and_strategy_adjustment',scheduled_review='Broad review214 completed; next mandatory strategy/current-literature review217 after214--216.')
assert not validate_campaign(m,g,root=root)
write('state/active_campaign.yml',m)
write('state/next_round_plan.yml',dict(round_index=215,status='active',campaign_id=cid,starting_graph_sha256=h,predecessor_round=214,tasks=[t['id'] for t in tasks]))
lp=Path('state/round_ledger.yml');raw=lp.read_bytes();s=raw.decode();ledger=json.loads(s)
assert ledger['rounds'][-1]['round_index']==214 and ledger['rounds'][-1]['status']=='closed'
entry=dict(round_index=215,campaign_id=cid,type=m['round_type'],status='active',objective=m['frozen_target']['question'],tasks=[{k:t[k] for k in ['id','role','status']} for t in tasks],resource_policy=m['resource_policy'],starting_graph_sha256=h,exit_labels=m['exit_labels'],started_at=now)
eol='\r\n' if '\r\n' in s else '\n';marker=eol+'  ]'+eol+'}';head,tail=s.rsplit(marker,1)
new=head+','+eol+eol.join('    '+line for line in json.dumps(entry,indent=2).splitlines())+marker+tail
new=new.replace('"active_round": 214','"active_round": 215',1);ledger['active_round']=215;ledger['rounds'].append(entry);assert json.loads(new)==ledger
put(lp,new.encode())
matrix=read('state/validation_matrix.yml');matrix.update(campaign_id=cid,promotion_status='round_215_active_no_promotion',graph_sha256=h,decision_rule='Complete actual localized wave attack; no estimate accepted at launch.')
for t in tasks:matrix['gates'].append(dict(id='round215_'+t['id'],status='pending',artifact=t['report_path']))
matrix['gates'].append(dict(id='round215_conductor_reconciliation',status='pending',artifact=base.as_posix()+'/reviews/conductor_round215_reconciliation.md'))
write('state/validation_matrix.yml',matrix)
write(base/'controls/starting_state_hashes.json',{p:sha(p) for p in ['state/proof_obligations.yml','state/best_proof_draft.md','strategy/gauss_circle_strategy_review_2026-09-23.md']})
failure=Path('state/failure_ledger.md');oldbytes=failure.read_bytes();prepare_campaign(m,g,root=root,graph_path=root/'state/proof_obligations.yml')
put(failure,oldbytes+b'\n\n## Round215 barriers\n\nThe complete weighted localized wave momentC215 is unproved. Retain actual common modulations and all narrow/aligned packets, windows, tails and spatial norms. The unweighted cone theorem is not a free weighted-measure result; the214 generic cap/trace moment is insufficient. Positive radius/centering certificates remain scoped failures, not signed lower bounds. Full quarter and every M1/M2/GAR/endpoint alternative stay open. A new identity without a complete quantitative gain does not solve the moment.\n')
write(base/'controls/frozen_artifact_hashes.json',{p.as_posix():sha(p) for p in [base/'plan.json',Path(strategy)]+sorted((base/'briefs').glob('*.md'))})
for t in m['tasks']:t['status']='running'
write('state/active_campaign.yml',m);assert not validate_campaign(m,g,root=root)
print('Round215 frozen once; closed214 archive verified; three briefs ready; graph399 unchanged.')
