"""Freeze222 once after verified closed221; never rerun after success."""
import hashlib,json,sys,time
from pathlib import Path
from datetime import datetime,timezone
root=Path.cwd();sys.path.insert(0,str(root))
from math_collab.campaigns import validate_campaign,prepare_campaign
from math_collab.proof_obligations import load_graph,validate_graph
cid='m9-m2-complete-unbalanced-vector';base=Path('rounds/codex-managed')/cid
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def put(p,b):
 for i in range(5):
  try:Path(p).write_bytes(b);return
  except OSError:
   if i==4:raise
   time.sleep(.2)
def write(p,o):put(p,(json.dumps(o,indent=2,ensure_ascii=False)+'\n').encode())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
old=read('state/active_campaign.yml');assert old['round_index']==221 and old['status']=='complete'
archive=read('rounds/codex-managed/gc-actual-vector-gram-correlations/controls/artifact_hashes.json');assert len(archive)==27
for p,h in archive.items():assert sha(p)==h,p
assert not (base/'plan.json').exists()
g=load_graph(Path('state/proof_obligations.yml'));assert len(g['proof_obligations'])==401 and not validate_graph(g,root=root)
h=sha('state/proof_obligations.yml');assert h==old['closing_assessment']['resulting_graph_sha256']
strategy='strategy/round222_complete_unbalanced_vector_attack.md';now=datetime.now(timezone.utc).isoformat()
for d in ['briefs','reports','candidates','reviews','controls']:(base/d).mkdir(parents=True,exist_ok=True)
common=['protocol.md','state/proof_obligations.yml','state/active_campaign.yml',strategy,
base.as_posix()+'/briefs/conductor_actual_unbal_interface.md',
'strategy/gauss_circle_strategy_checkpoint_round220_2026-09-28.md',
'rounds/codex-managed/gc-actual-vector-gram-correlations/synthesis.md',
'rounds/codex-managed/m9-frequency-phase-diagram/reports/dual_three_quarter_attack.md',
'proofs/kernels/m9_m2_unbalanced_inverse_selector_reciprocity_projective_obstruction.md']
specs=[
('joint_cross_modulus_attack','discovery','selected_context',
'Attack the COMPLETE actual smooth residual M2 UNBAL target T_(L,K)<< (LK)^(3/4)X^epsilon for K=XL/D^2,K/L>16. Test one serious joint cross-modulus/frequency correlation mechanism retaining the literal actual (g,n,j,h) vector and both chi4 directions before a modulus triangle. Derive and estimate its complete output, not an unestimated matrix grant. Complete-period Farey/Kloosterman orthogonality is not a short-window theorem; pay every completion length, row-dependent Fourier weight, coefficient norm, large frequency, gcd stratum, real-centre factor and literal endpoint. A flat-component gain does not close the complete target unless all companions are paid. Do not repeat160 scalarization or143 positive row closure as a new mechanism. Restore the full physical powers and compare the flat envelope only in its valid scope. Seven sections, one mechanism, no experiments, no sibling/shared-state/successor work; report and stop.',
common+['rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reports/level_four_kloosterman_embedding_attack.md','rounds/codex-managed/gc-full-goal-arithmetic-source-review/reports/blind_smooth_mask.md','rounds/codex-managed/gc-full-goal-arithmetic-source-review/reviews/conductor_smooth_mask_review.md']),
('actual_product_phase_attack','discovery','selected_context',
'Attack the SAME COMPLETE actual M2 UNBAL target through one serious joint product-phase arithmetic/differencing mechanism on the original h,k vector. Preserve chi4(h), the actual slanted Vaaler symbol, both quarter shifts and real signs before estimating the joint output. A mixed h,k differencing or joint phase-correlation method is allowed, but derive all amplitudes and shifts and attempt a signed estimate; do not grant a positive mean-square target, erase the character and cite a known one-variable bound as new, or treat the product-grouped irregular divisor coefficient as smooth. Pay all ranges, profiles, floors/stars, support entries/exits and transform boundary modules; do not promote a flat-only statement as complete. Restore a quantitative complete bound or exact failed-certificate powers and first gap. No unproved source import, only one serious mechanism, zero experiments, seven sections, no sibling/shared-state/successor work; stop after assigned report.',common),
('blind_cross_modulus','blind_rederiver','statement_only',
'Read only protocol and the isolated finite packet. Derive complete-common-period and arbitrary-window Kloosterman correlations, all gcd and inverse-representative cases, the distinct odd near-frequency control and unit-row-twist operator scope. No arithmetic application or source theorem. Seven sections with prior-history disclosure, zero experiments/web, only assigned report; stop.',
['protocol.md',base.as_posix()+'/briefs/blind_cross_modulus_statement.md'])]
controls=['complete_actual_unbal_owner','correct_K_and_phase','both_character_directions','literal_profiles_endpoints','all_gcd_and_frequency_rows','fixed_vector_vs_all_vectors','complete_vs_short_period','norm_and_restored_power','source_hypotheses','statement_only_derivation','full_goal_scope']
tasks=[]
for ident,role,mode,target,ctx in specs:
 t=dict(id=ident,role=role,access_mode=mode,status='pending',target=target,context_files=ctx,required_controls=controls,required_output=['Seven numbered protocol sections: result, exact hypotheses, proof/derivation, first gap, controls, dependencies/provenance, state effect.','Only assigned report; no shared edits, synthesis, sibling read or successor. Stop after final hash.'],report_path=base.as_posix()+'/reports/'+ident+'.md')
 if mode=='statement_only':t['excluded_context']=['Every file except protocol and isolated statement; prior-agent history disclosed.']
 tasks.append(t)
m=dict(schema_version=1,round_index=222,round_type='complete_unbalanced_actual_vector_attack',campaign_id=cid,title='Complete M2 UNBAL actual vector and product-phase attack',status='active',max_concurrency=3,coordinator='Codex',starting_graph_sha256=h,generated_at=now,
resource_policy=dict(analytical_algebraic_minimum_percent=95,numerical_experimental_maximum_percent=5,planned_numerical_percent=0,budget='Two bounded one-mechanism complete-target attacks, one isolated finite report, one same-round review/repair cycle; zero planned experiments.'),
target_obligations=['GC-target','M9-M2','M9-M2-smooth-unbalanced-three-quarter-estimate'],
frozen_target=dict(question='Can a genuinely joint actual cross-modulus vector or product-phase correlation prove the complete M2 UNBAL three-quarter estimate after every cost?',reference_formula='T_(L,K)=sum chi4(h)a_(L,K)(h,k)e(sqrt(Xhk)) <<_epsilon (LK)^(3/4)X^epsilon, K=XL/D^2,K/L>16, every real X and literal smooth residual block.',quantities=['Actual Vaaler taper, both shifts/signs, profiles, floors, stars, support crossings and all transform boundary errors.','Physical quarter target for every actual smooth UNBAL block; flat identities have only their stated scope.','Flat strict envelope min(X^a,X^((1-a)/2)), a=delta-ell, and its missing quarter power are benchmarks only for the flat component.','Complete n,h matrices retain both characters, every gcd stratum, real centre, all long frequencies and moving endpoints.','Other M1/M2 parents, hard top endpoint, sufficient moment family and full quarter theorem remain open.']),
completion_criteria=['Two bounded complete-target attack reports and one statement-only finite correlation report.','Independent final-hash mathematical/application reviews and actual-versus-enlarged controls.','Complete quantitative gain or exact failed-certificate costs, synthesis, mechanically valid State Patch and222 closure.'],controls=controls,
exit_labels=['complete_unbal_vector_gain_requires_validation','complete_unbal_vector_attempt_no_new_bound'],tasks=tasks,
review_seams=[dict(id='cross_modulus_weighted_application',requirement='Actual joint coefficients, partial periods, gcd strata and full norms.'),dict(id='product_phase_character_and_endpoints',requirement='Exact sign/amplitude algebra and every parameter/endpoint range.'),dict(id='complete_owner_restoration',requirement='Correct physical normalization, no flat-to-complete scope enlargement, net restored powers.')],
previous_goal_turn_classification='progress_completed_reviewed_round_changes_next_action_no_complete_analytic_gain',scheduled_review='Mandatory broad strategy/current-primary review223 after220--222.')
assert not validate_campaign(m,g,root=root)
write('state/active_campaign.yml',m);write('state/next_round_plan.yml',dict(round_index=222,status='active',campaign_id=cid,starting_graph_sha256=h,predecessor_round=221,tasks=[t['id'] for t in tasks]))
lp=Path('state/round_ledger.yml');s=lp.read_text(encoding='utf-8');ledger=json.loads(s)
assert ledger['rounds'][-1]['round_index']==221 and ledger['rounds'][-1]['status']=='closed'
entry=dict(round_index=222,campaign_id=cid,type=m['round_type'],status='active',objective=m['frozen_target']['question'],tasks=[{k:t[k] for k in ['id','role','status']} for t in tasks],resource_policy=m['resource_policy'],starting_graph_sha256=h,exit_labels=m['exit_labels'],started_at=now)
marker='\n  ]\n}';head,tail=s.rsplit(marker,1);new=head+',\n'+'\n'.join('    '+line for line in json.dumps(entry,indent=2).splitlines())+marker+tail
new=new.replace('"active_round": 221','"active_round": 222',1);ledger['active_round']=222;ledger['rounds'].append(entry);assert json.loads(new)==ledger;put(lp,new.encode())
matrix=read('state/validation_matrix.yml');matrix.update(campaign_id=cid,promotion_status='round_222_active_no_promotion',graph_sha256=h,decision_rule='Complete actual UNBAL target; no vector or product-phase estimate accepted at launch.')
for t in tasks:matrix['gates'].append(dict(id='round222_'+t['id'],status='pending',artifact=t['report_path']))
matrix['gates'].append(dict(id='round222_conductor_reconciliation',status='pending',artifact=base.as_posix()+'/reviews/conductor_round222_reconciliation.md'));write('state/validation_matrix.yml',matrix)
write(base/'controls/starting_state_hashes.json',{p:sha(p) for p in ['state/proof_obligations.yml','state/best_proof_draft.md','strategy/gauss_circle_strategy_review_2026-09-23.md']})
failure=Path('state/failure_ledger.md');oldbytes=failure.read_bytes();prepare_campaign(m,g,root=root,graph_path=root/'state/proof_obligations.yml')
put(failure,oldbytes+b'\n\n## Round222 complete UNBAL vector barriers\n\nComplete target has K=XL/D^2 and phase e(sqrt(Xhk)). Smooth dual equivalence is not an estimate or hard-endpoint transfer. Flat107/118/143/160 identities and envelopes do not cover every literal companion. Complete h summation self-returns; scalarization, long-frequency compression, positive row norms and generic multiplier grants are already priced. Cross-modulus complete-period orthogonality is not a short or differently weighted row theorem. Retain actual characters and the full joint coefficient before a signed estimate, then restore every owner cost. No unestimated smaller complement or enlarged-vector counterexample closes the actual target.\n')
write(base/'controls/frozen_artifact_hashes.json',{p.as_posix():sha(p) for p in [base/'plan.json',Path(strategy)]+sorted((base/'briefs').glob('*.md'))})
for t in m['tasks']:t['status']='running'
write('state/active_campaign.yml',m);assert not validate_campaign(m,g,root=root)
write(base/'controls/dispatch_provenance.json',dict(round_index=222,frozen_objective_changed=False,agent_reuse={'joint_cross_modulus_attack':'/root/joint_divisor_kernel','actual_product_phase_attack':'/root/joint_lattice_kernel','blind_cross_modulus':'/root/full_frontier_sources'},isolation='Blind role reads only protocol and the isolated finite packet. Prior history disclosed; statement-only for this task, not history-free.',previous_turn_classification=m['previous_goal_turn_classification'],mathematical_numerical_experiments=0))
print('Round222 frozen; closed221 archive27 verified; graph401 unchanged; three bounded tasks ready.')
