"""Freeze224 after verified closed223. Never rerun after success."""
import hashlib,json,sys,time
from pathlib import Path
from datetime import datetime,timezone
root=Path.cwd();sys.path.insert(0,str(root))
from math_collab.campaigns import validate_campaign,prepare_campaign
from math_collab.proof_obligations import load_graph,validate_graph
cid='m9-m1-complete-gar-prime-amplification';base=Path('rounds/codex-managed')/cid
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def put(p,b):
 for i in range(5):
  try:Path(p).write_bytes(b);return
  except OSError:
   if i==4:raise
   time.sleep(.2)
def write(p,o):put(p,(json.dumps(o,indent=2,ensure_ascii=False)+'\n').encode())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
old=read('state/active_campaign.yml');assert old['round_index']==223 and old['status']=='complete'
assert not (base/'plan.json').exists()
entries=[e for e in read('state/round_ledger.yml')['rounds'] if 200<=e['round_index']<=223]
assert len(entries)==24 and all(e['status']=='closed' for e in entries)
count=0
for e in entries:
 for p,h in read(Path('rounds/codex-managed')/e['campaign_id']/'controls/artifact_hashes.json').items():
  assert sha(p)==h,p;count+=1
assert count==605
g=load_graph(Path('state/proof_obligations.yml'));assert len(g['proof_obligations'])==401 and not validate_graph(g,root=root)
h=sha('state/proof_obligations.yml');assert h==old['closing_assessment']['resulting_graph_sha256']
strategy='strategy/round224_complete_gar_split_prime_amplification.md';now=datetime.now(timezone.utc).isoformat()
for d in ['briefs','reports','candidates','reviews','controls']:(base/d).mkdir(parents=True,exist_ok=True)
common=['protocol.md','state/proof_obligations.yml','state/active_campaign.yml',strategy,
base.as_posix()+'/briefs/conductor_actual_gar_interface.md',
'strategy/gauss_circle_strategy_checkpoint_round223_2026-09-28.md',
'rounds/codex-managed/gc-full-goal-signed-source-review/synthesis.md',
'rounds/codex-managed/m9-m1-gar-radial-interface-reconciliation/candidates/conductor_terminal_height_interface_completion.md',
'rounds/codex-managed/m9-m1-global-lower-height-kernel-gate/candidates/conductor_profile_flattening_and_integer_phase.md',
'proofs/kernels/m9_m1_d1_full_abel_common_profile_recombination.md']
specs=[
('complete_signed_prime_attack','discovery','selected_context',
'Attempt the COMPLETE real GAR target for the exact A_X and F_X in the conductor packet using one split-prime Hecke amplification before separate norms. Derive all actual coefficient commutators and repeated-prime overlaps; keep the joint main-minus-commutator expression under its single real part. Attempt a quantitative complete cross-prime estimate with the actual chi4 divisor vector; optimize a stated amplifier range only with every norm, dilation, cutoff, profile, endpoint and reconstruction cost restored. Constants must be uniform in real X. No average over changed centres is a pointwise theorem. Do not replace A_X by1, discard commutators or grant arbitrary-vector orthogonality. If positivity or Cauchy is used, identify exactly where actual signs are lost and price the entire resulting certificate. Compare with the inherited COMPLETE estimate, keeping paid nonlower and all lower scales; a fragment, finite identity or newly named open norm is not a gain. At most one narrowly justified primary-source import audit if essential. Seven sections, zero experiments, one amplifier family, assigned report only, no current sibling/shared-state/successor work; stop with final hash.',
common+['state/best_proof_draft.md','rounds/codex-managed/m9-m1-global-angular-shifted-correlation/synthesis.md','rounds/codex-managed/m9-m1-reflected-mode-correlation/synthesis.md']),
('actual_prime_profile_control','seam_reviewer','selected_context',
'Independently control the complete actual A_X profile commutator in the proposed split-prime amplifier. Derive prime-shifted angular arguments, unchanged X-dependent heights, floors, hard stars and all overlap terms for p|n. Test whether the full correction is target-safe or whether its joint sign with the amplified term is indispensable; attempt a full estimate, not a locally cheap sector. If using lower flattening, include the physical error, complete range and later lower owners through159. Give actual-symbol controls when provable, distinguishing certificate mass from signed size and alternate arrays. Compare A_X(h,pq), A_X(ph,q), A_X(ph,pq) with A_X and with the INCORRECT substitution of coefficients at pX or X/p. Price the full parameter range of the tested amplifier and all physical restoration. No prime-count or source grant, no experiment, no current sibling/blind packet/shared-state/successor read or edit. Seven sections, one bounded mechanism, assigned report only; stop with final hash.',
common+['rounds/codex-managed/m9-m1-near-square-complementary-divisor-gate/synthesis.md','rounds/codex-managed/m9-m1-angular-mellin-separation/synthesis.md']),
('blind_prime_allocation','blind_rederiver','statement_only',
'Read only protocol and isolated statement. Independently derive coefficient allocation, exact overlap/commutator, adjoint identity, radial dilation factors and endpoints, constant-profile prime-power recurrence and the stated finite control. No application or source. Seven sections with prior-history disclosure, no experiments/web, assigned report only; stop.',
['protocol.md',base.as_posix()+'/briefs/blind_prime_allocation_statement.md'])]
controls=['complete_actual_gar_owner','exact_chi4_divisor_relation','prime_power_overlap','actual_profile_commutator','literal_floors_stars','real_pairing','radial_dilation_cutoffs','fixed_vs_scaled_centre','all_lower_scales','norm_and_physical_restoration','actual_vs_enlarged_control','statement_only_derivation','source_hypotheses_if_used','full_goal_scope']
tasks=[]
for ident,role,mode,target,ctx in specs:
 t=dict(id=ident,role=role,access_mode=mode,status='pending',target=target,context_files=ctx,required_controls=controls,required_output=['Seven numbered protocol sections: result, exact hypotheses, proof/derivation, first gap, controls, dependencies/provenance, state effect.','Only assigned report; no shared edits, synthesis, sibling access or successor. Stop after final SHA256.'],report_path=base.as_posix()+'/reports/'+ident+'.md')
 if mode=='statement_only':t['excluded_context']=['Every file except protocol and isolated statement; prior-agent history disclosed.']
 tasks.append(t)
m=dict(schema_version=1,round_index=224,round_type='complete_gar_split_prime_amplification',campaign_id=cid,title='Complete real GAR split-prime amplification',status='active',max_concurrency=3,coordinator='Codex',starting_graph_sha256=h,generated_at=now,
resource_policy=dict(analytical_algebraic_minimum_percent=95,numerical_experimental_maximum_percent=5,planned_numerical_percent=0,budget='Three bounded seven-section reports, one amplifier family, one same-round review/repair cycle; zero planned experiments. At most one narrow primary import audit if essential.'),
target_obligations=['GC-target','M9-M1-global-angular-radial-estimate','M9-M1-global-lower-radial-signed-estimate','M9-M1-GAR-total-active-equivalence'],
frozen_target=dict(question='Can split-prime amplification using the complete actual divisor-allocation relation and its profile commutators prove or quantitatively improve the complete real total-M1 GAR estimate?',
reference_formula='|Re{e(1/8) sum_(n<=16sqrt X) C_X^*(n)n^(-3/4)e(sqrt(Xn))}| << X^epsilon for every real X and exact fixed accepted profiles.',
quantities=['A_X(h,q)=sum_j1_(h<=H_j)Phi(h/(H_j+1))[w_j(2sqrt(Xh/q))]^*, D_j=2^(-j)floor(sqrt X), H_j=floor(D_j X^(-1/4)).',
'Complete Hecke main-minus-commutator expression, repeated-prime overlaps, both original signs, prime2 and all literal endpoints.',
'Exact factors p^(3/4), p^(-3/4), divisibility masks, shifted phases and cutoffs; A_X remains at the original prescribed centre.',
'Accepted120 nonlower estimate and every lower scale/dependency through159; no fragment or upper-certificate floor is a complete gain.',
'Physical factor -(4/pi)X^(1/4), owned transform errors and inactive bottom. GAR controls total M1 only; every M2/endpoint and full quarter remain open.']),
completion_criteria=['Complete signed amplification report, independent actual-profile control and statement-only finite allocation derivation.',
'Independent final-hash mathematical/application reviews and source audit only if a theorem is imported; all controls and full physical costs.',
'Complete gain or precise no-gain/failure statement, conductor synthesis, mechanically valid State Patch and224 closure before any successor.'],
controls=controls,exit_labels=['complete_gar_gain_requires_validation','complete_gar_amplification_no_new_bound'],tasks=tasks,
review_seams=[dict(id='prime_allocation_and_adjoint',requirement='All p-adic overlaps, character cases, phase/amplitude and integer endpoints.'),dict(id='actual_commutator_and_signed_estimate',requirement='Actual fixed-X profiles and complete main-minus-correction before norms; distinguish actual signed size from certificates.'),dict(id='complete_owner_restoration',requirement='All lower scales, exact real pairing, full physical powers, no total-to-blockwise or M1-to-full-target inference.')],
previous_goal_turn_classification='progress_completed_reviewed_strategy_round_changes_next_action_no_complete_analytic_gain',
scheduled_review='Next broad strategy/current-primary review226.')
assert not validate_campaign(m,g,root=root),validate_campaign(m,g,root=root)
write('state/active_campaign.yml',m);write('state/next_round_plan.yml',dict(round_index=224,status='active',campaign_id=cid,starting_graph_sha256=h,predecessor_round=223,tasks=[t['id'] for t in tasks]))
lp=Path('state/round_ledger.yml');s=lp.read_text(encoding='utf-8');ledger=json.loads(s)
assert ledger['rounds'][-1]['round_index']==223 and ledger['rounds'][-1]['status']=='closed'
entry=dict(round_index=224,campaign_id=cid,type=m['round_type'],status='active',objective=m['frozen_target']['question'],tasks=[{k:t[k] for k in ['id','role','status']} for t in tasks],resource_policy=m['resource_policy'],starting_graph_sha256=h,exit_labels=m['exit_labels'],started_at=now)
marker='\n  ]\n}';head,tail=s.rsplit(marker,1);new=head+',\n'+'\n'.join('    '+line for line in json.dumps(entry,indent=2).splitlines())+marker+tail
new=new.replace('"active_round": 223','"active_round": 224',1);ledger['active_round']=224;ledger['rounds'].append(entry);assert json.loads(new)==ledger;put(lp,new.encode())
matrix=read('state/validation_matrix.yml');matrix.update(campaign_id=cid,promotion_status='round_224_active_no_promotion',graph_sha256=h,decision_rule='Complete actual real GAR estimate; no amplified or commutator bound accepted at launch.')
for t in tasks:matrix['gates'].append(dict(id='round224_'+t['id'],status='pending',artifact=t['report_path']))
matrix['gates'].append(dict(id='round224_conductor_reconciliation',status='pending',artifact=base.as_posix()+'/reviews/conductor_round224_reconciliation.md'));write('state/validation_matrix.yml',matrix)
write(base/'controls/starting_state_hashes.json',{p:sha(p) for p in ['state/proof_obligations.yml','state/best_proof_draft.md','strategy/gauss_circle_strategy_review_2026-09-23.md']})
failure=Path('state/failure_ledger.md');oldbytes=failure.read_bytes();prepare_campaign(m,g,root=root,graph_path=root/'state/proof_obligations.yml')
put(failure,oldbytes+b'\n\n## Round224 complete GAR split-prime barriers\n\nActual angular coefficients are not unrestricted r2/4 Hecke eigenvectors. Keep all profile commutators and p-adic overlaps under the complete real pairing. Prime dilations retain amplitude factors, divisibility restrictions, changed radial cutoffs and phases at scaled centres while A_X stays fixed. No parameter average, cross-prime orthogonality, target-safe correction, or flat-to-complete bridge is granted. Retain accepted120 nonlower completion,121--122 exact lower reductions and later lower-owner dependencies through159. Complementary inversion, reflection, Fourier/Abel self-return and coefficient-blind positive norms alone are not a new gain. Full M2/endpoints and the quarter goal remain open.\n')
write(base/'controls/frozen_artifact_hashes.json',{p.as_posix():sha(p) for p in [base/'plan.json',Path(strategy)]+sorted((base/'briefs').glob('*.md'))})
for t in m['tasks']:t['status']='running'
write('state/active_campaign.yml',m);assert not validate_campaign(m,g,root=root)
write(base/'controls/dispatch_provenance.json',dict(round_index=224,frozen_objective_changed=False,agent_reuse={'complete_signed_prime_attack':'/root/full_frontier_sources','actual_prime_profile_control':'/root/joint_divisor_kernel','blind_prime_allocation':'/root/joint_lattice_kernel'},isolation='Blind task reads only protocol and isolated packet; previous history disclosed. Other tasks have minimal named context and cannot read current sibling reports.',previous_turn_classification=m['previous_goal_turn_classification'],mathematical_numerical_experiments=0))
print('Round224 frozen; all605 prior archive entries checked; graph401 unchanged; three bounded tasks ready.')
