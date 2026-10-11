"""Freeze228 after closed227. Never rerun after success."""
import hashlib,json,sys
from pathlib import Path
from datetime import datetime,timezone
root=Path.cwd();sys.path.insert(0,str(root))
from math_collab.campaigns import validate_campaign,prepare_campaign
from math_collab.proof_obligations import load_graph,validate_graph
cid='gc-signed-heegner-phase';base=Path('rounds/codex-managed')/cid
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def write(p,o):Path(p).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
old=read('state/active_campaign.yml');assert old['round_index']==227 and old['status']=='complete'
assert not (base/'plan.json').exists()
entries=[e for e in read('state/round_ledger.yml')['rounds'] if 200<=e['round_index']<=227]
assert len(entries)==28 and all(e['status']=='closed' for e in entries)
count=0
for e in entries:
 for p,h in read(Path('rounds/codex-managed')/e['campaign_id']/'controls/artifact_hashes.json').items():
  assert sha(p)==h,p;count+=1
assert count==732
g=load_graph(Path('state/proof_obligations.yml'));assert len(g['proof_obligations'])==401 and not validate_graph(g,root=root)
h=sha('state/proof_obligations.yml');assert h==old['closing_assessment']['resulting_graph_sha256']
strategy='strategy/round228_signed_heegner_phase.md';now=datetime.now(timezone.utc).isoformat()
for d in ['briefs','reports','reviews','candidates','controls']:(base/d).mkdir(parents=True,exist_ok=True)
prev='rounds/codex-managed/gc-complete-joint-spectral-remainder/'
common=['protocol.md','state/proof_obligations.yml','state/active_campaign.yml',strategy,
 'strategy/gauss_circle_strategy_review_2026-09-23.md','strategy/gauss_circle_strategy_checkpoint_round226_2026-09-28.md',
 base.as_posix()+'/briefs/complete_signed_heegner_interface.md',prev+'briefs/complete_joint_spectral_interface.md',
 prev+'reports/heegner_joint_norm_audit.md',prev+'reviews/independent_heegner_norm_review.md',
 prev+'reports/joint_shift_spectral_attack.md',prev+'reviews/independent_spectral_attack_review.md',prev+'synthesis.md',
 'proofs/kernels/gc_complete_square_root_large_values_moment_bound.md']
specs=[
 ('signed_hecke_functional_attack','discovery','selected_context',
 'Attack the COMPLETE signed cuspidal pairing in the exact level1/2 Heegner expression, with every shift, parity descendant, spectral mode and tail. Preserve its h^(it) times common spectral phase before norms. Investigate the exact Hecke L functional equation or equivalent Voronoi transformation at the resonant archimedean parameter; derive actual dual length, transform, root number, parity, conductor and old/new normalization. At the CM points check rather than assume any reflection/Fricke simplification. Seek an actual fully restored signed bound; a shorter formal dual polynomial alone is insufficient. Test any pretrace/geometric return for whether it simply recreates the original circle wave. At most one additional indispensable primary work with exact theorem audit, zero experiments. The continuous spectrum has a separate owner but remains in the FULL target; state the precise estimate needed for the full closure and retain prior complete cap if no gain. No current sibling or blind reads. Seven sections, assigned report only, freeze hash and stop.',common),
 ('complete_eisenstein_pairing','discovery','selected_context',
 'Own the ENTIRE continuous spectrum in the complete level1/2 Heegner remainder, not a local band. Derive exact Eisenstein values at i and (-1+i)/2, every cusp and fixed local factor. Test whether their actual CM Dirichlet-series mean values pay the raw A_J^2 N^(3/2)T^epsilon continuous target with every h<2N, parity descendant, both signs and spectral tails restored. Prove or exactly source all needed mean-value/functional-equation inputs; at most one additional indispensable primary work. Do not substitute a point cusp fourth moment or a generic local-Weyl price as a claimed gain. If continuous target is paid, quantify the remaining ENTIRE signed cusp term and explain why this alone does not prove a whole-wave gain. Also independently assess whether the exact geometric/pretrace recombination would recreate the original wave. No current sibling, blind or root control reads. Seven sections, zero experiments, assigned report only, final hash then stop.',common),
 ('blind_gamma_transition','blind_rederiver','statement_only',
 'Read ONLY protocol and isolated gamma-ratio packet. Independently derive factorization, all phase constants, near-transition uniform expansion and fixed-order derivative control, both transition centers and full-axis modulus envelope. Prove controls at critical sigma and v=0. No arithmetic applications, sources or experiments. Seven sections, only assigned report; disclose isolation, freeze hash and stop.',
 ['protocol.md',base.as_posix()+'/briefs/blind_gamma_transition_statement.md'])]
controls=['actual_full_target','all_shifts_parity_and_scales','signed_joint_phase_before_norms','source_and_functional_equation_hypotheses','complete_discrete_and_continuous_spectra','gamma_transitions_and_dual_lengths','literal_endpoints_and_tails','real_complex_scope','full_power_restoration','certificate_not_actual_lower_bound','statement_only_control','fixed_order_full_goal']
tasks=[]
for ident,role,mode,target,ctx in specs:
 t=dict(id=ident,role=role,access_mode=mode,status='pending',target=target,context_files=ctx,required_controls=controls,
 required_output=['Seven numbered sections: result, exact hypotheses, proof, first gap, controls, dependencies/provenance, state effect.','Write only assigned report; exact primary hypotheses for imports; final SHA256 then stop.'],report_path=base.as_posix()+'/reports/'+ident+'.md')
 if mode=='statement_only':t['excluded_context']=['All except protocol and isolated gamma statement; no arithmetic, source, sibling or history context.']
 tasks.append(t)
m=dict(schema_version=1,round_index=228,round_type='complete_signed_heegner_phase_attack',campaign_id=cid,title='Complete signed Heegner phase and continuous spectrum',status='active',max_concurrency=3,coordinator='Codex',starting_graph_sha256=h,generated_at=now,
 resource_policy=dict(analytical_algebraic_minimum_percent=95,numerical_experimental_maximum_percent=5,planned_numerical_percent=0,budget='Three bounded reports, one attack/assessment and one review/repair cycle; at most one additional indispensable primary work per nonblind role; zero experiments.'),
 target_obligations=old['target_obligations'],frozen_target=dict(question='Can the COMPLETE actual signed Heegner pairing gain by its resonant Hecke functional equation and a fully paid continuous spectrum?',reference_formula='Checkpoint226(F), exact whole-functional Heegner report227(7)--(10): complete signed raw remainder <= A_J^2 N^(3/2)T^epsilon, all h<2N and dyadicN<=P<2T^(3/2), every real R~T.',quantities=['Actual signed g_N and r2; all parity and old/new factors, all continuous cusps and discrete modes.','Exact growing transforms, dual lengths, gamma transitions, source hypotheses and fully reconstructed powers.','A paid full spectral component retains its entire complementary owner and is not a whole-wave gain.','Full quarter or genuinely stronger complete exponent remains the goal; beta only complete REAL.']),
 completion_criteria=['Complete discrete attack and complete continuous owner reports, plus isolated gamma derivation.','Nonauthor final-hash reviews of sources, transforms, full components and root application.','Full restored result or exact first unproved complete estimate, synthesis and valid State Patch before round229 design.'],
 controls=controls,exit_labels=['complete_signed_heegner_gain_requires_validation','complete_signed_heegner_no_new_bound'],tasks=tasks,
 review_seams=[dict(id='signed_hecke_transform',requirement='Actual dual transform, every parity/conductor/oldspace factor and full signed spectral estimate.'),dict(id='complete_eisenstein_estimate',requirement='All CM cusp values and source hypotheses, full mean-value bound and complete all-shift cost.'),dict(id='gamma_transition_application',requirement='Isolated uniform derivation and nonauthor application without false Stirling or cancellation.'),dict(id='full_goal_restoration',requirement='Every component, tail, complete owner and physical exponent restored.')],
 previous_goal_turn_classification=old['closing_assessment']['goal_turn_classification'],scheduled_review='Mandatory broad strategy/current-primary review229 after228 closure.')
assert not validate_campaign(m,g,root=root)
write('state/active_campaign.yml',m)
write('state/next_round_plan.yml',dict(round_index=228,status='active',campaign_id=cid,starting_graph_sha256=h,predecessor_round=227,tasks=[t['id'] for t in tasks]))
lp=Path('state/round_ledger.yml');s=lp.read_text(encoding='utf-8');ledger=json.loads(s)
assert ledger['rounds'][-1]['round_index']==227 and ledger['rounds'][-1]['status']=='closed'
entry=dict(round_index=228,campaign_id=cid,type=m['round_type'],status='active',objective=m['frozen_target']['question'],tasks=[{k:t[k] for k in ['id','role','status']} for t in tasks],resource_policy=m['resource_policy'],starting_graph_sha256=h,exit_labels=m['exit_labels'],started_at=now)
marker='\n  ]\n}';head,tail=s.rsplit(marker,1)
new=head+',\n'+'\n'.join('    '+line for line in json.dumps(entry,indent=2).splitlines())+marker+tail
new=new.replace('"active_round": 227','"active_round": 228',1)
ledger['active_round']=228;ledger['rounds'].append(entry);assert json.loads(new)==ledger;lp.write_bytes(new.encode())
matrix=read('state/validation_matrix.yml');matrix.update(campaign_id=cid,promotion_status='round_228_active_no_promotion',graph_sha256=h,decision_rule='Full signed spectral target frozen; separate complete components owned, no estimate accepted at launch.')
for t in tasks:matrix['gates'].append(dict(id='round228_'+t['id'],status='pending',artifact=t['report_path']))
matrix['gates'].append(dict(id='round228_conductor_reconciliation',status='pending',artifact=base.as_posix()+'/reviews/conductor_round228_reconciliation.md'))
write('state/validation_matrix.yml',matrix)
write(base/'controls/starting_state_hashes.json',{p:sha(p) for p in ['state/proof_obligations.yml','state/best_proof_draft.md','strategy/gauss_circle_strategy_review_2026-09-23.md']})
failure=Path('state/failure_ledger.md');oldbytes=failure.read_bytes()
prepare_campaign(m,g,root=root,graph_path=root/'state/proof_obligations.yml')
failure.write_bytes(oldbytes+b'\n\n## Round228 signed Heegner phase barriers\n\nAll732 closed200--227 archive entries verified. Previous turn changed the next analytical action through reviewed complete spectral evidence, not an improved bound. The exact Heegner functional avoids a false level4 coefficientwise point transfer. Its positive norms cost A^2 T N^2, even an optimistic free fixed-sieve-size comparison costs A^2 T N^(3/2), and the elementary A^2N^2 cap is better. Preserve actual h^(it) with the common spectral phase before norms. Resonant functional equations require every transition, parity, conductor, oldspace and dual reconstruction cost. A paid entire continuous spectrum does not pay its cusp partner. All full-proof owners remain open; upper certificates are not actual lower bounds. Mandatory broad review229.\n')
write(base/'controls/frozen_artifact_hashes.json',{p.as_posix():sha(p) for p in [base/'plan.json',Path(strategy)]+sorted((base/'briefs').glob('*.md'))})
for t in m['tasks']:t['status']='running'
write('state/active_campaign.yml',m);assert not validate_campaign(m,g,root=root)
write(base/'controls/dispatch_provenance.json',dict(round_index=228,frozen_objective_changed=False,agent_tasks=[t['id'] for t in tasks],isolation='Fresh fork_none task-specific agents; blind only protocol and isolated packet. No sibling reads before report freeze.',previous_turn_classification=m['previous_goal_turn_classification'],mathematical_numerical_experiments=0))
print('Round228 frozen; all732 prior archive entries verified; graph401 unchanged.')
