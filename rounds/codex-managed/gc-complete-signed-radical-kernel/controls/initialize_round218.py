"""Freeze218 once, from the verified closed217 state."""
import hashlib, json, sys, time
from pathlib import Path
from datetime import datetime, timezone
root=Path.cwd();sys.path.insert(0,str(root))
from math_collab.campaigns import validate_campaign,prepare_campaign
from math_collab.proof_obligations import load_graph,validate_graph
cid='gc-complete-signed-radical-kernel';base=Path('rounds/codex-managed')/cid
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def put(p,b):
 for i in range(5):
  try:Path(p).write_bytes(b);return
  except OSError:
   if i==4:raise
   time.sleep(.2)
def write(p,o):put(p,(json.dumps(o,indent=2,ensure_ascii=False)+'\n').encode())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
old=read('state/active_campaign.yml');assert old['round_index']==217 and old['status']=='complete'
prior=Path('rounds/codex-managed/gc-full-goal-distinct-source-review')
archive=read(prior/'controls/artifact_hashes.json');assert len(archive)==31
for p,h in archive.items():assert sha(p)==h,p
assert not (base/'plan.json').exists()
g=load_graph(Path('state/proof_obligations.yml'));assert len(g['proof_obligations'])==401 and not validate_graph(g,root=root)
h=sha('state/proof_obligations.yml');assert h==old['closing_assessment']['resulting_graph_sha256']
strategy='strategy/round218_complete_signed_radical_kernel.md';now=datetime.now(timezone.utc).isoformat()
for d in ['briefs','reports','candidates','reviews','controls']:(base/d).mkdir(parents=True,exist_ok=True)
common=['protocol.md','state/proof_obligations.yml','state/active_campaign.yml',strategy,
'strategy/gauss_circle_strategy_checkpoint_round217_2026-09-28.md',
'proofs/kernels/gc_complete_square_root_large_values_moment_bound.md',
'proofs/kernels/gc_complete_distinct_radical_moment_reduction.md',
'proofs/kernels/gc_distinct_radical_absolute_certificate_obstruction.md',
'rounds/codex-managed/gc-complete-signed-convolution-attack/synthesis.md',
'rounds/codex-managed/gc-signed-near-frequency-cancellation/synthesis.md']
specs=[
('joint_divisor_kernel','discovery','selected_context',
'Attack the COMPLETE actual I12 bound at29/25 by retaining the chi4 product and complex displaced Fourier kernel through a joint multivariable divisor calculation. Seek a new joint signed saving; keep all twelve signs, distinct squarefree masks, harmonics, unequal blocks, endpoints, tails and derivative costs. The216 equivalence permits the full B twelfth moment, but not an unproved mask-smoothness shortcut. Prove the complete bound or diagnose this one mechanism with restored powers and an explicit first unproved step. Old scalar absolute CRT/Poisson and free density subtraction already fail; do not relabel them as progress. One bounded report, at most one primary theorem audit if necessary, zero experiments, stop after seven sections.',common),
('joint_lattice_kernel','discovery','selected_context',
'Attack the COMPLETE actual I12 bound at29/25 via the exact Gaussian-integer interpretation of r2 and joint high-dimensional Poisson/stationary phase before separate norms. Test whether the joint radial phase and common R give a genuine dimension gain. Preserve angular/radial stationary degeneracies, actual integer dual multiplicities, mixed signs, unequal norm blocks, nonproduct amplitudes, endpoints and full tails. If replacing the distinct mask, use only the paid216 full-moment equivalence. Derive a complete estimate or quantitatively diagnose this mechanism, not a new unestimated sector. Scalar Poisson costs from203 and localized-wave evidence below are inherited barriers. At most one primary theorem audit, zero experiments, seven sections and stop.',
common+['rounds/codex-managed/gc-complete-localized-wave-moment/synthesis.md']),
('blind_joint_radial','blind_rederiver','statement_only',
'Independently solve the isolated joint-radial oscillatory-integral packet, including exact stationary dimension, uniform mismatch, all signs and sharpness. Read only protocol and packet; no arithmetic origin or other context. Seven sections, zero experiments, assigned report only, then stop.',
['protocol.md',base.as_posix()+'/briefs/blind_joint_radial_statement.md'])]
controls=['actual_coefficients','all_distinct_class_masks','full_signed_kernel','joint_stationary_geometry','unequal_blocks','all_harmonics_signs_tails','real_endpoints','complete_norm_cost','old_barrier_bypass','statement_only_control','fixed_order_full_goal_scope']
tasks=[]
for ident,role,mode,target,ctx in specs:
 t=dict(id=ident,role=role,access_mode=mode,status='pending',target=target,context_files=ctx,required_controls=controls,required_output=['Seven numbered protocol sections: result; exact hypotheses; proof; first gap; controls; exact dependencies; state effect.','Write only assigned report; no shared state, synthesis, sibling or successor work.'],report_path=base.as_posix()+'/reports/'+ident+'.md')
 if mode=='statement_only':t['excluded_context']=['Everything except protocol and isolated packet, including generated brief, graph, manifest, strategy, siblings, history and web.']
 tasks.append(t)
m=dict(schema_version=1,round_index=218,round_type='complete_actual_signed_kernel_attack',campaign_id=cid,title='Complete actual joint signed radical-kernel attack',status='active',max_concurrency=3,coordinator='Codex',starting_graph_sha256=h,generated_at=now,
resource_policy=dict(analytical_algebraic_minimum_percent=95,numerical_experimental_maximum_percent=5,planned_numerical_percent=0,budget='Three bounded reports; one complete mechanism per discovery task; at most one primary theorem audit per task if needed; one same-round seam cycle; zero experiments planned.'),
target_obligations=['GC-target','GC-complete-distinct-radical-twelfth-reduction','GC-distinct-radical-absolute-certificate-obstruction'],
frozen_target=dict(question='Can joint divisor or Gaussian-integer lattice cancellation bound the COMPLETE actual signed I12 at29/25, with every complement and restored power paid?',reference_formula='I12(T,floor(T^(2/5)))<=C_epsilon T^(29/25+epsilon), equivalent by216 to M12(B_T) at the same power.',quantities=['Actual a_n=r2(n)n^(-3/4)Psi(sqrt(n/T)) and displaced w(R/T), all ordered twelve-distinct squarefree classes and every harmonic/sign/block/tail.','Complete full-B twelfth moment is an allowed equivalent route; the arithmetic mask cannot be differentiated as a smooth weight.','Ambient high dimension does not imply full-rank stationary phase; all radial null directions and actual dual-shell multiplicities must be priced.','The fixed target is only102/325; full quarter still requires a sufficient unbounded-fixed-order family or complete alternative parents.']),
completion_criteria=['Three bounded seven-section reports and important isolated joint-radial derivation.','Complete actual norm/power costs or a precisely scoped no-go for each specified method.','Independent final-hash mathematical/application seams and conductor reproduction.','Validated State Patch and recorded218 closure before any successor design.'],
controls=controls,exit_labels=['complete_signed_moment_gain_requires_validation','complete_joint_kernel_attempt_no_new_bound'],tasks=tasks,
review_seams=[dict(id='joint_radial_geometry',requirement='Exact stationary sets, rank, mismatch uniformity, unequal scales, smooth seminorms and sharpness.'),dict(id='actual_arithmetic_transfer',requirement='Actual r2/chi4, masks, integer dual multiplicity, every sign/block/tail and complete power.'),dict(id='full_goal_scope',requirement='Actual signed estimate versus certificate; fixed milestone versus unbounded family; no old barrier relabeling.')],
previous_goal_turn_classification='progress_round217_validated_obstruction_and_changed_strategy_no_complete_moment_gain',scheduled_review='Next mandatory broad strategy/current-primary-literature review220 after217--219.')
assert not validate_campaign(m,g,root=root)
write('state/active_campaign.yml',m)
write('state/next_round_plan.yml',dict(round_index=218,status='active',campaign_id=cid,starting_graph_sha256=h,predecessor_round=217,tasks=[t['id'] for t in tasks]))
lp=Path('state/round_ledger.yml');s=lp.read_text(encoding='utf-8');ledger=json.loads(s)
assert ledger['rounds'][-1]['round_index']==217 and ledger['rounds'][-1]['status']=='closed'
entry=dict(round_index=218,campaign_id=cid,type=m['round_type'],status='active',objective=m['frozen_target']['question'],tasks=[{k:t[k] for k in ['id','role','status']} for t in tasks],resource_policy=m['resource_policy'],starting_graph_sha256=h,exit_labels=m['exit_labels'],started_at=now)
marker='\n  ]\n}';head,tail=s.rsplit(marker,1)
new=head+',\n'+'\n'.join('    '+line for line in json.dumps(entry,indent=2).splitlines())+marker+tail
new=new.replace('"active_round": 217','"active_round": 218',1);ledger['active_round']=218;ledger['rounds'].append(entry);assert json.loads(new)==ledger
put(lp,new.encode())
matrix=read('state/validation_matrix.yml');matrix.update(campaign_id=cid,promotion_status='round_218_active_no_promotion',graph_sha256=h,decision_rule='Complete actual joint signed-kernel attack; no new estimate accepted at launch.')
for t in tasks:matrix['gates'].append(dict(id='round218_'+t['id'],status='pending',artifact=t['report_path']))
matrix['gates'].append(dict(id='round218_conductor_reconciliation',status='pending',artifact=base.as_posix()+'/reviews/conductor_round218_reconciliation.md'))
write('state/validation_matrix.yml',matrix)
write(base/'controls/starting_state_hashes.json',{p:sha(p) for p in ['state/proof_obligations.yml','state/best_proof_draft.md','strategy/gauss_circle_strategy_review_2026-09-23.md']})
failure=Path('state/failure_ledger.md');oldbytes=failure.read_bytes();prepare_campaign(m,g,root=root,graph_path=root/'state/proof_obligations.yml')
put(failure,oldbytes+b'\n\n## Round218 joint signed-kernel barriers\n\nThe complete distinct positive certificate is at leastT^(5/2); its signed target remains open. Preserve original kernel phases, actual chi4 and integer dual multiplicities. The squarefree mask is not smooth. Full ambient dimension is not stationary-phase rank. Old203 scalar Poisson/free centering and210 absolute CRT costs must be bypassed by a new joint signed estimate, not merely renamed. The paid216 equivalence permits the full actual B moment, with no smaller complement substituted.\n')
write(base/'controls/frozen_artifact_hashes.json',{p.as_posix():sha(p) for p in [base/'plan.json',Path(strategy)]+sorted((base/'briefs').glob('*.md'))})
for t in m['tasks']:t['status']='running'
write('state/active_campaign.yml',m);assert not validate_campaign(m,g,root=root)
print('Round218 frozen once; closed217 archive31 verified; graph401 unchanged; three briefs ready.')
