"""Freeze223 after verified closed222. Never rerun after success."""
import hashlib,json,sys,time
from pathlib import Path
from datetime import datetime,timezone
root=Path.cwd();sys.path.insert(0,str(root))
from math_collab.campaigns import validate_campaign,prepare_campaign
from math_collab.proof_obligations import load_graph,validate_graph
cid='gc-full-goal-signed-source-review';base=Path('rounds/codex-managed')/cid
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def put(p,b):
 for i in range(5):
  try:Path(p).write_bytes(b);return
  except OSError:
   if i==4:raise
   time.sleep(.2)
def write(p,o):put(p,(json.dumps(o,indent=2,ensure_ascii=False)+'\n').encode())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
old=read('state/active_campaign.yml');assert old['round_index']==222 and old['status']=='complete'
assert not (base/'plan.json').exists()
entries=[e for e in read('state/round_ledger.yml')['rounds'] if 200<=e['round_index']<=222]
assert len(entries)==23 and all(e['status']=='closed' for e in entries)
count=0
for e in entries:
 for p,h in read(Path('rounds/codex-managed')/e['campaign_id']/'controls/artifact_hashes.json').items():
  assert sha(p)==h,p;count+=1
assert count==574
g=load_graph(Path('state/proof_obligations.yml'));assert len(g['proof_obligations'])==401 and not validate_graph(g,root=root)
h=sha('state/proof_obligations.yml');assert h==old['closing_assessment']['resulting_graph_sha256']
strategy='strategy/round223_full_goal_signed_source_review.md';now=datetime.now(timezone.utc).isoformat()
for d in ['briefs','reports','candidates','reviews','controls']:(base/d).mkdir(parents=True,exist_ok=True)
common=['protocol.md','state/proof_obligations.yml','state/active_campaign.yml',strategy,
'strategy/gauss_circle_strategy_review_2026-09-23.md',
'strategy/gauss_circle_strategy_checkpoint_round220_2026-09-28.md',
'rounds/codex-managed/m9-m2-complete-unbalanced-vector/synthesis.md',
'rounds/codex-managed/gc-actual-vector-gram-correlations/synthesis.md']
specs=[
('multiplicative_wave_sources','source_auditor','selected_context',
'Current primary-source and complete whole-wave/moment strategy review, at most TWO exact theorem audits. Start by checking Robles2609.11070v1 Theorem1.1/Corollary1.1 against actual r2 coefficients, their mean square, the large-squarefree mask and square-root phase; a fixed source coefficient constant cannot grow without a proved dependence, and logarithmic savings are not fixed-power savings. Scope-screen a genuinely distinct nonlinear multiplicative or high-value source for a second audit if justified. Give exact links, versions, theorem hypotheses, actual coefficients and full phase/norm/exceptional-set/tail/pointwise restoration, or the first failed premise. Keep all real R, actual mollifier, all harmonics and unequal blocks. A fixed twelfth milestone is not quarter; preserve the sufficient unbounded FIXED even-order family and both inherited high-value terms. No generic arbitrary-vector or phase-transfer grant. Recommend one complete source-compatible next inequality, without starting it. Seven sections, at most two full audits, zero experiments; no sibling/shared-state/successor work; report and stop.',
common+['proofs/kernels/gc_complete_square_root_large_values_moment_bound.md','proofs/kernels/gc_complete_distinct_radical_moment_reduction.md','rounds/codex-managed/gc-full-goal-arithmetic-source-review/reports/full_frontier_sources.md']),
('geometric_complete_frontiers','source_auditor','selected_context',
'Bounded current-primary and complete M1/M2/GAR frontier review, at most TWO exact theorem audits. Read graph/draft owners and compare complete M1 HARD with all small-t/large-G terms, independent SMOOTH, M2 TOP/BAL/UNBAL, and total-M1 GAR plus M2. Scope-screen methods outside failed positive/scalar closures, especially exact Pascadi2511.08445 current non-abelian amplification and Fouvry-Kowalski-Michel-Sawin2511.09459 current trace-function geometry, checking actual primary records and theorem text before use. These are leads, not mandated imports. Audit only a source with a concrete kernel map; keep modulus/factorization/unit/conductor/monodromy restrictions, exceptional and prime-power/2-adic complements, actual coefficient/product norms, interval masks, all aliases/endpoints and outer absolute values. State complete net exponents or exact first failed hypothesis. Do not repeat220 paid source transfers or call222 upper prices universal lower barriers. Recommend one complete quantified next objective and the actual signed structure it would exploit, not another indefinitely unestimated fragment. Seven sections; no experiments, sibling/shared-state/successor work; report and stop.',
common+['state/best_proof_draft.md','rounds/codex-managed/m9-m1-t1-complete-source-coefficient-mask-analysis/synthesis.md','proofs/kernels/m9_m2_unbalanced_inverse_selector_reciprocity_projective_obstruction.md','rounds/codex-managed/gc-full-goal-arithmetic-source-review/reports/reciprocal_energy_sources.md','rounds/codex-managed/gc-full-source-method-review/reports/bilinear_arithmetic_sources.md']),
('blind_oscillatory_transfer','blind_rederiver','statement_only',
'Read only protocol and isolated packet. Independently prove the smooth curved chirp Fourier-L1 bounds, exact discrete periodization and weighted transfer, and the one-sample alias control. Distinguish absolute continuous certificate, signed periodization, actual sample and optimal discrete norms. Seven sections, prior-history disclosure, no web/experiments; assigned report only and stop.',
['protocol.md',base.as_posix()+'/briefs/blind_oscillatory_transfer_statement.md'])]
controls=['current_primary_versions','exact_theorem_hypotheses','actual_coefficient_class','complete_phase_and_kernel','all_frontiers','coefficient_and_transfer_norms','exceptional_moduli_and_frequencies','literal_endpoints_and_tails','full_power_restoration','actual_vs_enlarged_scope','statement_only_control','fixed_unbounded_order_scope']
tasks=[]
for ident,role,mode,target,ctx in specs:
 t=dict(id=ident,role=role,access_mode=mode,status='pending',target=target,context_files=ctx,required_controls=controls,required_output=['Seven numbered protocol sections: result, exact hypotheses, proof/derivation, first gap, controls, dependencies/provenance, state effect.','Exact primary URLs, versions and theorem numbers for source claims; only assigned report, no shared edits, synthesis, sibling or successor. Stop after final hash.'],report_path=base.as_posix()+'/reports/'+ident+'.md')
 if mode=='statement_only':t['excluded_context']=['Every file except protocol and isolated statement; prior-agent history disclosed.']
 tasks.append(t)
m=dict(schema_version=1,round_index=223,round_type='mandatory_full_goal_signed_source_review',campaign_id=cid,title='Full-goal signed arithmetic and oscillatory source review',status='active',max_concurrency=3,coordinator='Codex',starting_graph_sha256=h,generated_at=now,
resource_policy=dict(analytical_algebraic_minimum_percent=95,numerical_experimental_maximum_percent=5,planned_numerical_percent=0,budget='Three bounded reports, at most two full audits per source role, one same-round review/repair cycle, zero planned experiments.'),
target_obligations=['GC-target','M9-M1','M9-M2','GC-complete-square-root-large-values-moment-bound','GC-complete-distinct-radical-twelfth-reduction'],
frozen_target=dict(question='Does any exactly applicable current source or changed signed mechanism advance a complete full-proof frontier after220--222, and which complete quantified target should be attempted next?',reference_formula='Full goal P(X)<<X^(1/4+epsilon), all complete M1/M2/GAR frontiers and the sufficient unbounded FIXED even-moment family. No complete gain from local components, positive certificates or logarithmic savings alone.',quantities=['Actual coefficients, signs, real centres, all moduli/aliases, masks, profiles, endpoints and tails in every proposed application.','The fixed I12(T,floor(T^(2/5)))<=T^(29/25+epsilon) milestone supplies102/325, not quarter.','Correct UNBAL K=XL/D^2 and phase e(sqrt(Xhk)); flat scopes and hard endpoints remain separate.','Continuous absolute Fourier transfer, signed periodization and optimal discrete norms are distinct.']),
completion_criteria=['Two bounded current-primary/full-frontier source reports and one isolated oscillatory-transfer report.','Independent final-hash source, mathematical and application reviews; exact controls, complete costs and strategy checkpoint.','A verified complete gain or explicit no-gain strategy decision, synthesis, mechanically valid State Patch and223 closure before any successor.'],controls=controls,
exit_labels=['complete_signed_source_gain_requires_validation','strategy_signed_source_review_no_complete_gain'],tasks=tasks,
review_seams=[dict(id='source_and_actual_full_kernel',requirement='Primary theorem text, exact actual coefficients and phase, all exclusions, norms and costs.'),dict(id='isolated_fourier_transfer',requirement='Statement-only proof and exact application, without transferring its lower certificate to signed periodization.'),dict(id='full_goal_strategy',requirement='Every complete frontier, unchanged qualified benchmark, sufficient unbounded fixed-order scope and one justified next objective.')],
previous_goal_turn_classification='progress_completed_reviewed_round_changes_method_selection_no_complete_analytic_gain',scheduled_review='Mandatory review223 after220--222; next broad strategy/current-primary review226.')
assert not validate_campaign(m,g,root=root)
write('state/active_campaign.yml',m);write('state/next_round_plan.yml',dict(round_index=223,status='active',campaign_id=cid,starting_graph_sha256=h,predecessor_round=222,tasks=[t['id'] for t in tasks]))
lp=Path('state/round_ledger.yml');s=lp.read_text(encoding='utf-8');ledger=json.loads(s)
assert ledger['rounds'][-1]['round_index']==222 and ledger['rounds'][-1]['status']=='closed'
entry=dict(round_index=223,campaign_id=cid,type=m['round_type'],status='active',objective=m['frozen_target']['question'],tasks=[{k:t[k] for k in ['id','role','status']} for t in tasks],resource_policy=m['resource_policy'],starting_graph_sha256=h,exit_labels=m['exit_labels'],started_at=now)
marker='\n  ]\n}';head,tail=s.rsplit(marker,1);new=head+',\n'+'\n'.join('    '+line for line in json.dumps(entry,indent=2).splitlines())+marker+tail
new=new.replace('"active_round": 222','"active_round": 223',1);ledger['active_round']=223;ledger['rounds'].append(entry);assert json.loads(new)==ledger;put(lp,new.encode())
matrix=read('state/validation_matrix.yml');matrix.update(campaign_id=cid,promotion_status='round_223_active_no_promotion',graph_sha256=h,decision_rule='Complete full-proof source review; no theorem or actual signed gain accepted at launch.')
for t in tasks:matrix['gates'].append(dict(id='round223_'+t['id'],status='pending',artifact=t['report_path']))
matrix['gates'].append(dict(id='round223_conductor_reconciliation',status='pending',artifact=base.as_posix()+'/reviews/conductor_round223_reconciliation.md'));write('state/validation_matrix.yml',matrix)
write(base/'controls/starting_state_hashes.json',{p:sha(p) for p in ['state/proof_obligations.yml','state/best_proof_draft.md','strategy/gauss_circle_strategy_review_2026-09-23.md']})
failure=Path('state/failure_ledger.md');oldbytes=failure.read_bytes();prepare_campaign(m,g,root=root,graph_path=root/'state/proof_obligations.yml')
put(failure,oldbytes+b'\n\n## Round223 full-goal signed source barriers\n\nComplete220 source costs,221 fixed-vector/positive-correlation failures and222 weighted constant-mode/rectangle certificate losses are retained. No complete bound improved. A logarithmic source saving is not a fixed-power improvement; actual r2 and radical-mask coefficients must satisfy the exact source class, with constants controlled. Continuous Fourier-L1 transfer and its signed periodization are different objects. All exceptional moduli, real phases, endpoints, tails, product norms and reconstruction costs remain. Do not promote a source resemblance or a smaller complement. Compare every full M1/M2/GAR and fixed-unbounded-moment route before selecting one complete next target.\n')
write(base/'controls/frozen_artifact_hashes.json',{p.as_posix():sha(p) for p in [base/'plan.json',Path(strategy)]+sorted((base/'briefs').glob('*.md'))})
for t in m['tasks']:t['status']='running'
write('state/active_campaign.yml',m);assert not validate_campaign(m,g,root=root)
write(base/'controls/dispatch_provenance.json',dict(round_index=223,frozen_objective_changed=False,agent_reuse={'multiplicative_wave_sources':'/root/full_frontier_sources','geometric_complete_frontiers':'/root/joint_divisor_kernel','blind_oscillatory_transfer':'/root/joint_lattice_kernel'},isolation='Blind current task reads only protocol and isolated packet. Prior history disclosed; not history-free.',previous_turn_classification=m['previous_goal_turn_classification'],mathematical_numerical_experiments=0))
print('Round223 frozen; all574 protected archive entries verified; graph401 unchanged; three bounded tasks ready.')
