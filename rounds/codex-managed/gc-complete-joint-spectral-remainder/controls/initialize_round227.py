"""Freeze227 after verified closed226. Never rerun after success."""
import hashlib,json,sys
from pathlib import Path
from datetime import datetime,timezone
root=Path.cwd();sys.path.insert(0,str(root))
from math_collab.campaigns import validate_campaign,prepare_campaign
from math_collab.proof_obligations import load_graph,validate_graph
cid='gc-complete-joint-spectral-remainder';base=Path('rounds/codex-managed')/cid
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def write(p,o):Path(p).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
old=read('state/active_campaign.yml');assert old['round_index']==226 and old['status']=='complete'
assert not (base/'plan.json').exists()
entries=[e for e in read('state/round_ledger.yml')['rounds'] if 200<=e['round_index']<=226]
assert len(entries)==27 and all(e['status']=='closed' for e in entries)
count=0
for e in entries:
 for p,h in read(Path('rounds/codex-managed')/e['campaign_id']/'controls/artifact_hashes.json').items():
  assert sha(p)==h,p;count+=1
assert count==701
g=load_graph(Path('state/proof_obligations.yml'));assert len(g['proof_obligations'])==401 and not validate_graph(g,root=root)
h=sha('state/proof_obligations.yml');assert h==old['closing_assessment']['resulting_graph_sha256']
strategy='strategy/round227_complete_joint_spectral_remainder.md';now=datetime.now(timezone.utc).isoformat()
for d in ['briefs','reports','reviews','candidates','controls']:(base/d).mkdir(parents=True,exist_ok=True)
prev='rounds/codex-managed/gc-full-goal-spectral-source-review/'
common=['protocol.md','state/proof_obligations.yml','state/active_campaign.yml',strategy,
 'strategy/gauss_circle_strategy_review_2026-09-23.md','strategy/gauss_circle_strategy_checkpoint_round226_2026-09-28.md',
 base.as_posix()+'/briefs/complete_joint_spectral_interface.md',prev+'reports/actual_shifted_spectral_sources.md',
 prev+'reviews/independent_shifted_source_review.md',prev+'synthesis.md',
 'proofs/kernels/gc_complete_square_root_large_values_moment_bound.md']
specs=[
 ('joint_shift_spectral_attack','discovery','selected_context',
 'Attack the COMPLETE signed remainder(F), not a selected shift range. Derive its actual joint h/spectral expression from HKLDW1705.04771v3 with exact r2 weights, density subtraction, zero atom, every discrete and continuous term and justified contours. Preserve the h sum and oscillatory Mellin kernel together; derive a quantitative oscillatory estimate if possible, using the actual coefficient vector rather than arbitrary moduli. Analyze joint stationary phases including gamma/Bessel phases and decide whether they create useful cancellation or return the original wave. At most one additional indispensable primary theorem may be audited with full hypotheses; AH2607.13518v1 is already an allowed lead, not a granted bridge. Restore every h<2N, all dyadic N<=P, spectral tails, normalization and physical exponent. End with a complete gain or exact first unproved joint inequality plus fully priced applicable norm menu. Do not repeat226 absolute Abel, elementary221 completion, a local transform identity, or an unestimated complement as progress. Seven sections, exact source citations, zero experiments, only assigned report, freeze and stop.',common),
 ('heegner_joint_norm_audit','seam_reviewer','selected_context',
 'Independently test the actual Heegner spectral coefficient/norm interface for COMPLETE remainder(F). Read AH2607.13518v1 proof of the r2 application and its cited identities as needed, and HKLDW1705.04771v3. Derive a valid identification or an exact failed hypothesis between point-value fourth moments and the actual regularized-theta pairing; do not grant their equality. Seek an independently useful full joint kernel formulation from the actual r2 Hecke geometry. Apply only exactly matched spectral estimates, retaining all h, test-transform dependence, continuous/discrete spectra and endpoints. Price the strongest applicable collective spectral Holder/Cauchy/large-sieve menu and compare its fully restored complete exponent with beta and quarter. At most one additional indispensable exact primary theorem audit. If no complete bound, identify the actual remaining vector norm and quantify the missing saving, not merely say a transfer is unavailable. No current sibling or blind reads, no arbitrary-array lower bound as actual no-go. Seven sections, zero experiments, assigned report only, freeze and stop.',common+['state/best_proof_draft.md','rounds/codex-managed/gc-complete-logarithmic-convolution/synthesis.md']),
 ('blind_mellin_phase','blind_rederiver','statement_only',
 'Read ONLY protocol and isolated statement packet. Independently derive stationary set, uniform curvature, leading phase, weighted Mellin absolute-mass order, all boundary/empty/limit controls and certificate-versus-signed scope. No sources or arithmetic application. Seven sections, exact dependencies and history disclosure, zero experiments, assigned report only; freeze and stop.',
 ['protocol.md',base.as_posix()+'/briefs/blind_mellin_phase_statement.md'])]
controls=['actual_coefficients_and_density','all_shifts_and_scales','joint_phase_before_norms','source_hypotheses_and_coefficient_bridge','continuous_and_discrete_spectra','spectral_and_mellin_heights','literal_endpoints_and_tails','real_complex_scope','full_power_restoration','actual_vs_certificate_scope','statement_only_control','fixed_order_full_goal']
tasks=[]
for ident,role,mode,target,ctx in specs:
 t=dict(id=ident,role=role,access_mode=mode,status='pending',target=target,context_files=ctx,required_controls=controls,
 required_output=['Seven numbered protocol sections: result, exact hypotheses, proof, first gap, controls, dependencies/provenance, recommended state effect.','Only assigned report; exact theorem/version/source hypotheses for imports. Final SHA256 then stop.'],
 report_path=base.as_posix()+'/reports/'+ident+'.md')
 if mode=='statement_only':t['excluded_context']=['All except protocol and isolated packet; no current source or application context.']
 tasks.append(t)
m=dict(schema_version=1,round_index=227,round_type='complete_signed_spectral_remainder_attack',campaign_id=cid,
 title='Complete actual joint shifted-correlation spectral remainder',status='active',max_concurrency=3,coordinator='Codex',starting_graph_sha256=h,generated_at=now,
 resource_policy=dict(analytical_algebraic_minimum_percent=95,numerical_experimental_maximum_percent=5,planned_numerical_percent=0,
 budget='Three bounded reports; one analytic attack/assessment cycle and one review/repair cycle; at most one additional indispensable source theorem per nonblind role; zero experiments.'),
 target_obligations=['GC-target','M9-M1','M9-M2','GC-complete-square-root-large-values-moment-bound','GC-complete-distinct-radical-twelfth-reduction'],
 frozen_target=dict(question='Can the COMPLETE actual signed all-shift Fejer remainder gain through a joint spectral estimate with every norm and reconstruction cost paid?',
 reference_formula='Checkpoint226(F): 2Re sum_{1<=h<2N}(1-h/(2N))[C_h-rho_h integral W_h] <= A_J(N)^2 N^(3/2) T^epsilon, all dyadic2<=N<=P, P smallest dyadic>=T^(3/2), every real R~T.',
 quantities=['Actual r2, signed fixed Psi, every overlap and full continuous density even at discrete-empty shifts.','Complete complex sufficient target, inherited beta only complete REAL; full quarter remains objective.','Every discrete/continuous spectral term, exact coefficient identities, Mellin heights, contour residues, all tails and physical restoration.','No fixed moment, local shift sector, formal identity or large positive certificate accepted as complete gain.']),
 completion_criteria=['Two orthogonal complete spectral attack/norm reports and isolated elementary Mellin-phase derivation.','Independent final-hash source/coefficient/kernel/application reviews and fully restored complete cost.','Validated complete gain or exact first unproved full estimate; conductor synthesis and valid State Patch before successor228.'],
 controls=controls,exit_labels=['complete_joint_spectral_gain_requires_validation','complete_joint_spectral_remainder_no_new_bound'],tasks=tasks,
 review_seams=[dict(id='actual_joint_spectral_kernel',requirement='Actual r2 weights, all h, exact density, legitimate contour and all spectral components.'),dict(id='heegner_coefficient_and_norm',requirement='Exact point/pairing coefficient identity and complete costs of every spectral norm.'),dict(id='mellin_phase_application',requirement='Isolated phase derivation, uniform stationary and tail bounds, nonauthor actual application.'),dict(id='full_goal_restoration',requirement='All scales, tails, real/complex scope and physical exponent with every alternative owner retained.')],
 previous_goal_turn_classification='progress_completed_reviewed_source_evidence_changes_next_action_no_complete_analytic_gain',scheduled_review='Next broad strategy/current-primary checkpoint229.')
assert not validate_campaign(m,g,root=root)
write('state/active_campaign.yml',m)
write('state/next_round_plan.yml',dict(round_index=227,status='active',campaign_id=cid,starting_graph_sha256=h,predecessor_round=226,tasks=[t['id'] for t in tasks]))
lp=Path('state/round_ledger.yml');s=lp.read_text(encoding='utf-8');ledger=json.loads(s)
assert ledger['rounds'][-1]['round_index']==226 and ledger['rounds'][-1]['status']=='closed'
entry=dict(round_index=227,campaign_id=cid,type=m['round_type'],status='active',objective=m['frozen_target']['question'],tasks=[{k:t[k] for k in ['id','role','status']} for t in tasks],resource_policy=m['resource_policy'],starting_graph_sha256=h,exit_labels=m['exit_labels'],started_at=now)
marker='\n  ]\n}';head,tail=s.rsplit(marker,1)
new=head+',\n'+'\n'.join('    '+line for line in json.dumps(entry,indent=2).splitlines())+marker+tail
new=new.replace('"active_round": 226','"active_round": 227',1)
ledger['active_round']=227;ledger['rounds'].append(entry);assert json.loads(new)==ledger;lp.write_bytes(new.encode())
matrix=read('state/validation_matrix.yml');matrix.update(campaign_id=cid,promotion_status='round_227_active_no_promotion',graph_sha256=h,decision_rule='Full joint spectral target frozen; no estimate accepted at launch.')
for t in tasks:matrix['gates'].append(dict(id='round227_'+t['id'],status='pending',artifact=t['report_path']))
matrix['gates'].append(dict(id='round227_conductor_reconciliation',status='pending',artifact=base.as_posix()+'/reviews/conductor_round227_reconciliation.md'))
write('state/validation_matrix.yml',matrix)
write(base/'controls/starting_state_hashes.json',{p:sha(p) for p in ['state/proof_obligations.yml','state/best_proof_draft.md','strategy/gauss_circle_strategy_review_2026-09-23.md']})
failure=Path('state/failure_ledger.md');oldbytes=failure.read_bytes()
prepare_campaign(m,g,root=root,graph_path=root/'state/proof_obligations.yml')
failure.write_bytes(oldbytes+b'\n\n## Round227 complete joint spectral barriers\n\nAll701 closed200--226 archive entries verified. Previous turn completed reviewed source evidence changing the next action, but no complete analytic gain. The target is the entire signed Fejer remainder, all shifts and scales. Round226 already prices absolute Abel and straight-ray heat majorants. Direct spectral work must preserve the actual coefficient/test pairing and pay every continuous/discrete term, height, residue, endpoint and tail. AH point fourth moments do not automatically bound the HKLDW regularized-theta pairing; derive the identity or identify the failed premise. Upper certificate losses are not actual lower bounds. Full quarter, sufficient unbounded fixed-order moments and all M1/M2/GAR/endpoints remain open.\n')
write(base/'controls/frozen_artifact_hashes.json',{p.as_posix():sha(p) for p in [base/'plan.json',Path(strategy)]+sorted((base/'briefs').glob('*.md'))})
for t in m['tasks']:t['status']='running'
write('state/active_campaign.yml',m);assert not validate_campaign(m,g,root=root)
write(base/'controls/dispatch_provenance.json',dict(round_index=227,frozen_objective_changed=False,
 agent_tasks=[t['id'] for t in tasks],isolation='New task-specific agents use fork_turns none; blind current inputs protocol and isolated packet only. No current sibling reads before initial reports freeze.',
 previous_turn_classification=m['previous_goal_turn_classification'],mathematical_numerical_experiments=0))
print('Round227 frozen; all701 prior archive entries verified; graph401 unchanged.')
