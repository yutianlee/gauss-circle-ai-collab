"""Freeze round216 once, after readback of the closed215 archive."""
import hashlib,json,sys,time
from pathlib import Path
from datetime import datetime,timezone
root=Path.cwd();sys.path.insert(0,str(root))
from math_collab.campaigns import validate_campaign,prepare_campaign
from math_collab.proof_obligations import load_graph,validate_graph
cid='gc-actual-radical-high-values';base=Path('rounds/codex-managed')/cid
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def put(p,b):
 for i in range(5):
  try:Path(p).write_bytes(b);return
  except OSError:
   if i==4:raise
   time.sleep(.2)
def write(p,o):put(p,(json.dumps(o,indent=2,ensure_ascii=False)+'\n').encode())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
old=read('state/active_campaign.yml');assert old['round_index']==215 and old['status']=='complete'
prior=Path('rounds/codex-managed/gc-complete-localized-wave-moment')
archive=read(prior/'controls/artifact_hashes.json');assert len(archive)==25
for p,h in archive.items():assert sha(p)==h,p
assert not (base/'plan.json').exists()
g=load_graph(Path('state/proof_obligations.yml'));assert len(g['proof_obligations'])==399 and not validate_graph(g,root=root)
h=sha('state/proof_obligations.yml');assert h==old['starting_graph_sha256']
strategy='strategy/round216_actual_radical_high_values.md';now=datetime.now(timezone.utc).isoformat()
for d in ['briefs','reports','candidates','reviews','controls']:(base/d).mkdir(parents=True,exist_ok=True)
common=['protocol.md','state/proof_obligations.yml','state/active_campaign.yml',strategy,'strategy/gauss_circle_strategy_checkpoint_round214_2026-09-28.md',prior.as_posix()+'/synthesis.md','proofs/kernels/gc_complete_square_root_large_values_moment_bound.md','rounds/codex-managed/gc-complete-signed-tenth-moment/reports/actual_tenth_high_values.md','rounds/codex-managed/gc-full-frontier-moment-strategy-review/controls/conductor_arithmetic_source_gate.md']
specs=[
('actual_radical_tail','discovery','selected_context',
'Attack the complete actual full-series twelfth high-value gateH216 by the exact squarefree-class cutoffQ=floor(T^(2/5)), retaining every s, sign, repeated class, unequal block, nonpairing relation, high-event cost and smoothing tail. Prove the low-class bound and seek an actual signed nonzero-correlation or complete high-tail estimate. Exact relations alone, arbitrary-array controls and a new unestimated remainder are not an arithmetic gain. At most one relevant primary theorem interface, audited completely. Seven sections; write only assigned report and stop.',common+['proofs/kernels/gc_weighted_square_root_exact_resonance_mass.md']),
('anchored_divisor_high_values','discovery','selected_context',
'AttackH216 through one actual divisor or fixed-vector projection mechanism preserving the absolute R~T anchor before Cauchy loses it. Keep actual r2, both cosine signs, all blocks and tails. Do not repeat the209 centered-L1 or translation-invariant Gram failure. Seek a complete quantitative high-value gain; if none, give the exact first failed arithmetic estimate and complete costs. The squarefree cutoff is optional for this independent route. At most one relevant primary theorem interface. Seven sections; write only assigned report and stop.',common),
('blind_radical_cutoff','blind_rederiver','statement_only',
'Independently derive the isolated squarefree-cutoff packet, exact resonance mass, complete high-event transfer and precise remaining signed scope. Read only protocol and isolated packet; no web or other context. Seven sections; write only assigned report and stop.',
['protocol.md',base.as_posix()+'/briefs/blind_radical_cutoff_statement.md'])]
controls=['actual_coefficients','absolute_radius_anchor','all_cosine_signs','squarefree_exact_nonzero_distinction','d1_and_nonpairing','all_s_and_integer_cutoff','high_event_threshold_constants','all_blocks_and_schwartz_tails','signed_certificate_distinction','source_hypotheses','real_endpoints','restored_powers','full_quarter_scope','statement_only_control']
tasks=[]
for ident,role,mode,target,ctx in specs:
 t=dict(id=ident,role=role,access_mode=mode,status='pending',target=target,context_files=ctx,required_controls=controls,required_output=['Seven numbered protocol sections: result; exact hypotheses; proof; first gap; controls; dependencies; state effect.','Write only assigned report; no siblings, state, synthesis or successor work.'],report_path=base.as_posix()+'/reports/'+ident+'.md')
 if mode=='statement_only':t['excluded_context']=['Everything except protocol and isolated packet, including generated general brief, graph, manifest, strategy, all reports, sources and web.']
 tasks.append(t)
m=dict(schema_version=1,round_index=216,round_type='complete_actual_radical_high_values',campaign_id=cid,title='Complete physical high values with actual radical coefficients',status='active',max_concurrency=3,coordinator='Codex',starting_graph_sha256=h,generated_at=now,
resource_policy=dict(analytical_algebraic_minimum_percent=95,numerical_experimental_maximum_percent=5,planned_numerical_percent=0,budget='Three bounded reports; at most one primary import per discovery role; one same-round review cycle; zero experiments planned.'),
target_obligations=['GC-target','GC-complete-square-root-large-values-moment-bound','GC-weighted-square-root-exact-resonance-mass','M9-M1','M9-M2'],
frozen_target=dict(question='Prove, quantitatively improve toward, or rigorously delimit the complete actual full-series twelfth high-value gateH216, preserving the full-quarter goal.',reference_formula='H12(T)=integral_(|B_T|>T^(13/125)) w(R/T)|B_T(R)|^12dR << T^(29/25+epsilon), with the exact full mollified r2 cosine series B_T.',quantities=['RealT>=2; Psi is the Fourier transform of a fixed nonnegative real radial unit-mass smooth mollifier supported in the unit disk; w>=0 smooth supported[1/2,2], equal1 on[1/sqrt(2),sqrt(3)].','B_T=sum_(n>=1)r2(n)n^(-3/4)Psi(sqrt(n/T))cos(2pi R sqrt(n)-3pi/4), every block, sign and Schwartz tail.','New interface n=d s^2, d squarefree, Q=floor(T^(2/5)); L_Q uses d<=Q and Z_Q all d>Q. Prove the head and complete high-event transfer; no free independence or exact-to-near inference.','Accepted204 pays low values; H216 success gives only102/325. Fullquarter requires a complete sufficient family or alternative parents.']),
completion_criteria=['Three bounded seven-section reports, including an isolated important radical-cutoff derivation.','Actual coefficient estimates or precisely scoped failures with complete high-event, scale and tail costs.','Independent final-hash seams and conductor full-goal synthesis.','Validated State Patch and closed ledger before mandatory review217 design; no unsupported arithmetic promotion.'],controls=controls,
exit_labels=['complete_actual_high_value_gain_requires_validation','complete_actual_high_value_gate_open'],tasks=tasks,
review_seams=[dict(id='radical_high_event_transfer',requirement='Squarefree cutoff, exact coefficients, signs, high-event inclusion and every infinite tail.'),dict(id='anchored_arithmetic',requirement='Absolute-radius information, actual divisor weights and complete bounds with first gap.'),dict(id='conductor_complete_power_scope',requirement='All low/high values, exact/nonzero separation, milestone and fullquarter scope.')],
previous_goal_turn_classification='progress_completed_and_validated215_changed_next_action_no_mathematical_gain',scheduled_review='Next mandatory broad strategy/current-literature review217 after214--216.')
assert not validate_campaign(m,g,root=root)
write('state/active_campaign.yml',m)
write('state/next_round_plan.yml',dict(round_index=216,status='active',campaign_id=cid,starting_graph_sha256=h,predecessor_round=215,tasks=[t['id'] for t in tasks]))
lp=Path('state/round_ledger.yml');raw=lp.read_bytes();s=raw.decode();ledger=json.loads(s)
assert ledger['rounds'][-1]['round_index']==215 and ledger['rounds'][-1]['status']=='closed'
entry=dict(round_index=216,campaign_id=cid,type=m['round_type'],status='active',objective=m['frozen_target']['question'],tasks=[{k:t[k] for k in ['id','role','status']} for t in tasks],resource_policy=m['resource_policy'],starting_graph_sha256=h,exit_labels=m['exit_labels'],started_at=now)
eol='\r\n' if '\r\n' in s else '\n';marker=eol+'  ]'+eol+'}';head,tail=s.rsplit(marker,1)
new=head+','+eol+eol.join('    '+line for line in json.dumps(entry,indent=2).splitlines())+marker+tail
new=new.replace('"active_round": 215','"active_round": 216',1);ledger['active_round']=216;ledger['rounds'].append(entry);assert json.loads(new)==ledger
put(lp,new.encode())
matrix=read('state/validation_matrix.yml');matrix.update(campaign_id=cid,promotion_status='round_216_active_no_promotion',graph_sha256=h,decision_rule='Complete actual high-value attack; no estimate accepted at launch.')
for t in tasks:matrix['gates'].append(dict(id='round216_'+t['id'],status='pending',artifact=t['report_path']))
matrix['gates'].append(dict(id='round216_conductor_reconciliation',status='pending',artifact=base.as_posix()+'/reviews/conductor_round216_reconciliation.md'))
write('state/validation_matrix.yml',matrix)
write(base/'controls/starting_state_hashes.json',{p:sha(p) for p in ['state/proof_obligations.yml','state/best_proof_draft.md','strategy/gauss_circle_strategy_review_2026-09-23.md']})
failure=Path('state/failure_ledger.md');oldbytes=failure.read_bytes();prepare_campaign(m,g,root=root,graph_path=root/'state/proof_obligations.yml')
put(failure,oldbytes+b'\n\n## Round216 barriers\n\nThe complete actual high-value targetH216 remains open. Squarefree independence proves exact relations only, not finite-time independence or near-frequency cancellation. The fixed cutoffQ=T^(2/5) must retain all s, signs, unequal blocks and smoothing tails. Pay the entire high-event transfer. Generic norm/Gram bounds erase the absolute-radius anchor; centered L1 and positive Fourier certificates remain parked. Random-model exceptional sets and qualitative thin-box correlations do not prove power-level tails. Fullquarter and all M1/M2/GAR/endpoint alternatives stay open.\n')
write(base/'controls/frozen_artifact_hashes.json',{p.as_posix():sha(p) for p in [base/'plan.json',Path(strategy)]+sorted((base/'briefs').glob('*.md'))})
for t in m['tasks']:t['status']='running'
write('state/active_campaign.yml',m);assert not validate_campaign(m,g,root=root)
print('Round216 frozen once; closed215 archive25 verified; graph399 unchanged; three briefs ready.')
