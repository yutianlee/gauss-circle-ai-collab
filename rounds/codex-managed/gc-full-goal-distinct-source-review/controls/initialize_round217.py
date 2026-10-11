"""Freeze mandatory review217 after verifying closed216."""
import hashlib,json,sys,time
from pathlib import Path
from datetime import datetime,timezone
root=Path.cwd();sys.path.insert(0,str(root))
from math_collab.campaigns import validate_campaign,prepare_campaign
from math_collab.proof_obligations import load_graph,validate_graph
cid='gc-full-goal-distinct-source-review';base=Path('rounds/codex-managed')/cid
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def put(p,b):
 for i in range(5):
  try:Path(p).write_bytes(b);return
  except OSError:
   if i==4:raise
   time.sleep(.2)
def write(p,o):put(p,(json.dumps(o,indent=2,ensure_ascii=False)+'\n').encode())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
old=read('state/active_campaign.yml');assert old['round_index']==216 and old['status']=='complete'
prior=Path('rounds/codex-managed/gc-actual-radical-high-values')
archive=read(prior/'controls/artifact_hashes.json');assert len(archive)==29
for p,h in archive.items():assert sha(p)==h,p
assert not (base/'plan.json').exists()
g=load_graph(Path('state/proof_obligations.yml'));assert len(g['proof_obligations'])==400 and not validate_graph(g,root=root)
h=sha('state/proof_obligations.yml');assert h==old['closing_assessment']['resulting_graph_sha256']
strategy='strategy/round217_full_goal_distinct_source_review.md';now=datetime.now(timezone.utc).isoformat()
for d in ['briefs','reports','candidates','reviews','controls']:(base/d).mkdir(parents=True,exist_ok=True)
common=['protocol.md','state/proof_obligations.yml','state/active_campaign.yml',strategy,
'strategy/gauss_circle_strategy_review_2026-09-23.md',
'strategy/gauss_circle_strategy_checkpoint_round214_2026-09-28.md',prior.as_posix()+'/synthesis.md',
'proofs/kernels/gc_complete_square_root_large_values_moment_bound.md',
'proofs/kernels/gc_complete_distinct_radical_moment_reduction.md']
specs=[
('distinct_correlation_sources','source_auditor','selected_context',
'Review current primary square-root/radical correlation, finite-window equidistribution, spacing and higher-moment methods for the literal actual twelve-distinct-class integral and a sufficient unbounded-fixed-order family. Fully audit at most two promising theorem interfaces. Retain growing squarefree classes, every harmonic, actual r2 coefficients, all signs, thin frequency scale, displaced window, unequal blocks and tails. Prove a complete quantitative consequence or identify the first exact failed hypothesis; generic independence and positive spacing are not signed estimates. Compare with the full-quarter goal. Write seven sections only to assigned report and stop; no siblings or successor work.',
common+['proofs/kernels/gc_weighted_square_root_exact_resonance_mass.md','rounds/codex-managed/gc-full-frontier-moment-strategy-review/controls/conductor_arithmetic_source_gate.md']),
('full_frontier_sources','source_auditor','selected_context',
'Review current primary arithmetic, bilinear, spectral, decoupling and large-value methods against every complete M1/M2/GAR and whole-physical-moment frontier, including the anchored divisor energy. Audit at most two promising exact theorem interfaces capable of changing the next action. Check current benchmark/source status, exact coefficients, variable lengths, norms, exceptional configurations and every restored power. Do not repeat named failed imports without a new premise. Recommend one complete quantitative direction and its full-quarter family; a theorem resemblance is not an application. Seven sections only to assigned report and stop; no siblings or successor work.',
common+[prior.as_posix()+'/reports/anchored_divisor_high_values.md',
'rounds/codex-managed/gc-full-proof-signed-arithmetic-review/reports/arithmetic_full_frontier.md',
'rounds/codex-managed/gc-full-goal-radius-source-review/reports/full_goal_harmonic_sources.md']),
('blind_moment_family','blind_rederiver','statement_only',
'Independently derive and optimize the isolated general-even-moment cutoff certificate, full partition costs and complete transfer. Distinguish its one-pass reach from a justified recursive use and its exact extra uniformity premises. Read only protocol and packet. No source, graph, manifest, strategy or sibling. Seven sections only to assigned report and stop.',
['protocol.md',base.as_posix()+'/briefs/blind_moment_family_statement.md'])]
controls=['actual_coefficients','distinct_repeated_class_scope','finite_window_not_torus','all_harmonics_signs_tails','source_versions_hypotheses','complete_norm_cost','real_endpoints','full_quarter_family','recursive_hypothesis_scope','signed_certificate_distinction','statement_only_control','complete_frontier']
tasks=[]
for ident,role,mode,target,ctx in specs:
 t=dict(id=ident,role=role,access_mode=mode,status='pending',target=target,context_files=ctx,required_controls=controls,required_output=['Seven numbered protocol sections: result; exact hypotheses; proof; first gap; controls; exact dependencies; state effect.','Write only assigned report; no shared state, synthesis, sibling or successor work.'],report_path=base.as_posix()+'/reports/'+ident+'.md')
 if mode=='statement_only':t['excluded_context']=['Everything except protocol and isolated packet, including generated general brief, graph, manifest, strategy, reports, sources and web.']
 tasks.append(t)
m=dict(schema_version=1,round_index=217,round_type='mandatory_full_goal_distinct_source_review',campaign_id=cid,title='Full-goal strategy and current sources after214--216',status='active',max_concurrency=3,coordinator='Codex',starting_graph_sha256=h,generated_at=now,
resource_policy=dict(analytical_algebraic_minimum_percent=95,numerical_experimental_maximum_percent=5,planned_numerical_percent=0,budget='Three bounded reports; at most two full primary theorem audits per source task; one same-round seam cycle; zero experiments planned.'),
target_obligations=['GC-target','M9-M1','M9-M2','GC-complete-square-root-large-values-moment-bound','GC-complete-distinct-radical-twelfth-reduction'],
frozen_target=dict(question='Which complete actual-coefficient objective should follow214--216 after current primary-source audits and full-goal comparison of the distinct-radical reduction with every alternative frontier?',reference_formula='P(X)<<X^(1/4+epsilon); complete physical moment family E(p)=1+o(p) or complete alternative parents, with I12 target29/25 only a milestone.',quantities=['Actual complete r2 cosine series, qualified Li--Yang input, all real endpoints, harmonics, signs and Schwartz tails.','Accepted216 head15/13 and repeated-class error8beta-1/5 pay only a reduction; distinct I12 remains unestimated.','Anchored divisor energy with rho<=208/2625 is an unproved sufficient input; all M1/M2/GAR alternatives remain.','General-even-moment cutoff analysis must distinguish optimized one-pass powers from recursive arguments with explicit availability premises.']),
completion_criteria=['Three bounded seven-section reports including an isolated important general-moment derivation.','Current primary-literature and complete-frontier audit, exact hypotheses, full cost ledger and one next objective.','Independent final-hash mathematical/source seams and conductor checkpoint/synthesis.','Validated State Patch and recorded217 closure before218 design.'],
controls=controls,exit_labels=['costed_full_goal_strategy_adjustment','new_complete_candidate_requires_validation'],tasks=tasks,
review_seams=[dict(id='general_moment_certificate',requirement='Every partition, head and tail cost, cutoff optimization, recursive availability, signed-integral transfer and full-goal limit.'),dict(id='current_source_application',requirement='Exact primary versions, actual coefficients, finite window, norms, exceptional regimes and complete power.'),dict(id='full_goal_selection',requirement='Complete frontier and one next quantified objective without shrinking quarter goal.')],
previous_goal_turn_classification='progress_new_complete_arithmetic_reduction216_validated_no_complete_moment_or_pointwise_gain',scheduled_review='Mandatory review217 after214--216; next broad review220 after217--219.')
assert not validate_campaign(m,g,root=root)
write('state/active_campaign.yml',m)
write('state/next_round_plan.yml',dict(round_index=217,status='active',campaign_id=cid,starting_graph_sha256=h,predecessor_round=216,tasks=[t['id'] for t in tasks]))
lp=Path('state/round_ledger.yml');s=lp.read_text(encoding='utf-8');ledger=json.loads(s)
assert ledger['rounds'][-1]['round_index']==216 and ledger['rounds'][-1]['status']=='closed'
entry=dict(round_index=217,campaign_id=cid,type=m['round_type'],status='active',objective=m['frozen_target']['question'],tasks=[{k:t[k] for k in ['id','role','status']} for t in tasks],resource_policy=m['resource_policy'],starting_graph_sha256=h,exit_labels=m['exit_labels'],started_at=now)
marker='\n  ]\n}';head,tail=s.rsplit(marker,1)
new=head+',\n'+'\n'.join('    '+line for line in json.dumps(entry,indent=2).splitlines())+marker+tail
new=new.replace('"active_round": 216','"active_round": 217',1);ledger['active_round']=217;ledger['rounds'].append(entry);assert json.loads(new)==ledger
put(lp,new.encode())
matrix=read('state/validation_matrix.yml');matrix.update(campaign_id=cid,promotion_status='round_217_active_no_promotion',graph_sha256=h,decision_rule='Mandatory broad full-goal source and strategy review; no estimate accepted at launch.')
for t in tasks:matrix['gates'].append(dict(id='round217_'+t['id'],status='pending',artifact=t['report_path']))
matrix['gates'].append(dict(id='round217_conductor_reconciliation',status='pending',artifact=base.as_posix()+'/reviews/conductor_round217_reconciliation.md'))
write('state/validation_matrix.yml',matrix)
write(base/'controls/starting_state_hashes.json',{p:sha(p) for p in ['state/proof_obligations.yml','state/best_proof_draft.md','strategy/gauss_circle_strategy_review_2026-09-23.md']})
failure=Path('state/failure_ledger.md');oldbytes=failure.read_bytes();prepare_campaign(m,g,root=root,graph_path=root/'state/proof_obligations.yml')
put(failure,oldbytes+b'\n\n## Round217 review barriers\n\nAccepted216 pays the actual small-class head and collective repeated classes, but its distinct signed integral remains open. Three-class near controls and whole-kernel absolute certificates are not distinct-class controls. Exact radical independence is not finite-window cancellation. The anchored divisor signed energy is unproved. Assess complete p-family and any recursive premises before claiming quarter reach. All full-proof alternatives and existing source repairs remain; re-audit current primary literature, not old labels.\n')
write(base/'controls/frozen_artifact_hashes.json',{p.as_posix():sha(p) for p in [base/'plan.json',Path(strategy)]+sorted((base/'briefs').glob('*.md'))})
for t in m['tasks']:t['status']='running'
write('state/active_campaign.yml',m);assert not validate_campaign(m,g,root=root)
print('Round217 frozen once; closed216 archive29 verified; graph400 unchanged; three briefs ready.')
