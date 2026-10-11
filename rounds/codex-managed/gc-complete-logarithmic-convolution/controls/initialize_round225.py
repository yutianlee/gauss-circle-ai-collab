"""Freeze225 only after verified closed224. Never rerun after success."""
import hashlib,json,sys,time
from pathlib import Path
from datetime import datetime,timezone
root=Path.cwd();sys.path.insert(0,str(root))
from math_collab.campaigns import validate_campaign,prepare_campaign
from math_collab.proof_obligations import load_graph,validate_graph
cid='gc-complete-logarithmic-convolution';base=Path('rounds/codex-managed')/cid
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def put(p,b):
 for i in range(5):
  try:Path(p).write_bytes(b);return
  except OSError:
   if i==4:raise
   time.sleep(.2)
def write(p,o):put(p,(json.dumps(o,indent=2,ensure_ascii=False)+'\n').encode())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
old=read('state/active_campaign.yml');assert old['round_index']==224 and old['status']=='complete'
assert not (base/'plan.json').exists()
entries=[e for e in read('state/round_ledger.yml')['rounds'] if 200<=e['round_index']<=224]
assert len(entries)==25 and all(e['status']=='closed' for e in entries)
count=0
for e in entries:
 for p,h in read(Path('rounds/codex-managed')/e['campaign_id']/'controls/artifact_hashes.json').items():
  assert sha(p)==h,p;count+=1
assert count==635
g=load_graph(Path('state/proof_obligations.yml'));assert len(g['proof_obligations'])==401 and not validate_graph(g,root=root)
h=sha('state/proof_obligations.yml');assert h==old['closing_assessment']['resulting_graph_sha256']
strategy='strategy/round225_complete_circle_logarithmic_convolution.md';now=datetime.now(timezone.utc).isoformat()
for d in ['briefs','reports','candidates','reviews','controls']:(base/d).mkdir(parents=True,exist_ok=True)
common=['protocol.md','state/proof_obligations.yml','state/active_campaign.yml',strategy,
 base.as_posix()+'/briefs/conductor_complete_circle_wave.md',
 'strategy/gauss_circle_strategy_checkpoint_round223_2026-09-28.md',
 'rounds/codex-managed/m9-m1-complete-gar-prime-amplification/synthesis.md',
 'rounds/codex-managed/gc-complete-signed-convolution-attack/synthesis.md',
 'proofs/kernels/gc_complete_square_root_large_values_moment_bound.md']
specs=[
 ('complete_nonlinear_prime_attack','discovery','selected_context',
 'Attempt the COMPLETE real circle wave uniformly at every real R in [cT,CT], with actual f=1*chi4, using exact f log=f*((1+chi4)Lambda) and one finite Vaughan decomposition family. Derive every short/long term for both character branches, literal U,V cutoffs and repeated prime powers; then seek a complete signed Type-I/Type-II estimate before arbitrary-coefficient Cauchy. Optimize U,V only after the entire decomposition is bounded with actual vector norms, product masks, real phase and all tails. Preserve n=1, divide by log only for n>=2, retain possible Psi sign changes and both cosine signs. Full target T^epsilon; inherited COMPLETE real baseline T^(beta+epsilon), beta=2theta_LY-1/2. A complex bound is sufficient if proved, not inherited. No average over R, favorable factor range, simple identity, source analogy or unestimated residual counts as a gain. Use exact physical sharp bridge and retain every mixed scale. At most one jointly coordinated narrow primary audit if essential; no broad survey. Seven sections; one bounded decomposition and review/repair cycle; zero experiments. Assigned report only, no sibling or blind reads, shared edits or successor; stop at final hash.',
 common+['rounds/codex-managed/gc-full-goal-signed-source-review/reports/multiplicative_wave_sources.md','rounds/codex-managed/gc-actual-radical-high-values/synthesis.md']),
 ('complete_factor_norm_audit','seam_reviewer','selected_context',
 'Independently derive and quantitatively test the COMPLETE logarithmic-convolution/Vaughan decomposition of the actual real circle wave in the conductor packet. Audit all f/chi4/Mobius/Lambda factors, short and long ranges, their actual l1/l2 norms, literal cutoff masks, logs, repeated prime powers, real-R uniformity, singleton and full Schwartz tail. Attempt a full nonlinear Type-I/Type-II estimate; if norms are used give the exact resulting exponent and compare to inherited beta. Identify actual signed arithmetic information lost in each closure; any adverse generic vector is not an arithmetic counterexample. All remaining terms must be bounded or explicitly left in the one complete missing inequality; do not create a chain of local survivors. The accepted unweighted exponent-pair kernel may be used only on a legal unweighted interval, with remaining norms restored. One narrow primary theorem audit is permitted if essential and coordinated with conductor; otherwise none. Seven sections, zero experiments. No current sibling/blind packet, shared edits or successor. Assigned report only; stop at final hash.',
 common+['sources/bourgain_2017_exponent_pair.md','rounds/codex-managed/gc-full-goal-signed-source-review/synthesis.md']),
 ('blind_finite_convolution','blind_rederiver','statement_only',
 'Read only protocol and isolated statement. Independently prove the logarithmic convolution, both character Vaughan branches, all prime powers and literal truncations, full finite contraction and controls. No application/source/experiment. Seven sections with retained-history disclosure, assigned report only; no shared state or successor; stop at final hash.',
 ['protocol.md',base.as_posix()+'/briefs/blind_finite_convolution_statement.md'])]
controls=['complete_actual_circle_wave','logarithmic_identity','both_character_branches','literal_vaughan_cutoffs','prime_powers_and_two','singleton_log_division','actual_product_norms','all_type_i_ii_ranges','real_radius_uniformity','cosine_and_complex_scope','schwartz_tail_and_mixed_scales','physical_sharp_reconstruction','statement_only_derivation','actual_vs_generic_control','source_hypotheses_if_used','full_goal_scope']
tasks=[]
for ident,role,mode,target,ctx in specs:
 t=dict(id=ident,role=role,access_mode=mode,status='pending',target=target,context_files=ctx,required_controls=controls,
 required_output=['Seven numbered protocol sections: result, exact hypotheses, proof/derivation, first gap, controls, dependencies/provenance, state effect.','Assigned report only, no shared edits, sibling access or successor; stop at final SHA256.'],
 report_path=base.as_posix()+'/reports/'+ident+'.md')
 if mode=='statement_only':t['excluded_context']=['All files except protocol and isolated statement; retained prior history disclosed.']
 tasks.append(t)
m=dict(schema_version=1,round_index=225,round_type='complete_circle_logarithmic_convolution',campaign_id=cid,
 title='Complete circle wave through logarithmic convolution',status='active',max_concurrency=3,coordinator='Codex',
 starting_graph_sha256=h,generated_at=now,
 resource_policy=dict(analytical_algebraic_minimum_percent=95,numerical_experimental_maximum_percent=5,planned_numerical_percent=0,
 budget='Three bounded seven-section reports; one logarithmic/Vaughan decomposition family; one same-round review/repair cycle; zero experiments. At most one coordinated narrow primary theorem audit if essential.'),
 target_obligations=['GC-target','GC-complete-square-root-large-values-moment-bound','GC-external-Li-Yang-theta-star'],
 frozen_target=dict(question='Can the exact logarithmic convolution and finite prime-factor decomposition yield a complete uniform bound for the actual circle wave better than the inherited beta, ultimately at T^epsilon?',
 reference_formula='sup_(R in [cT,CT]) |sum_(n>=1) r2(n)n^(-3/4)Psi(sqrt(n/T)) cos(2pi R sqrt(n)-3pi/4)| << T^epsilon.',
 quantities=['Fixed accepted mollifier Psi, every real T and R, n=1, all dyadic scales and complete infinite Schwartz tail.',
 'f=1*chi4=r2/4; f log=f*((1+chi4)Lambda); literal Vaughan cutoffs U,V and both branches with every prime power.',
 'Actual character/Mobius/divisor vectors and nonlinear phase R sqrt(product), product masks, all norms and both real signs.',
 'Complete inherited real exponent beta=2theta_LY-1/2; a complex bound is stronger and is not inherited.',
 'P(R^2)=sqrt(R)/pi B_T(R)+O(T^(1/2+epsilon)); target suffices for full quarter, intermediate gamma gives 1/4+gamma/2.',
 'Independent M1/M2/GAR and moment owners remain until a validated complete theorem discharges the target.']),
 completion_criteria=['Complete nonlinear attack and independent full parameter/norm audit, plus statement-only finite derivation.',
 'Independent final-hash algebra/application and source reviews if needed; all tails, actual coefficients and full physical costs checked.',
 'Complete gain or precise no-new-bound conclusion, conductor synthesis and valid State Patch; close225 before successor226.'],
 controls=controls,exit_labels=['complete_circle_wave_gain_requires_validation','complete_logarithmic_convolution_no_new_bound'],tasks=tasks,
 review_seams=[dict(id='finite_convolution',requirement='All signs, character branches, prime powers, truncation endpoints and finite contractions.'),
 dict(id='nonlinear_factor_estimates',requirement='Actual arithmetic vectors, all Type-I/II terms, product masks, source premises and complete parameter optimization.'),
 dict(id='complete_sharp_bridge',requirement='Real target, singleton, all scales/tails and physical exponent restoration.')],
 previous_goal_turn_classification='no_progress_on_complete_bounds_bounded_mechanism_closed_with_verified_controls',
 scheduled_review='Mandatory broad strategy/current-primary review226 after225.')
assert not validate_campaign(m,g,root=root),validate_campaign(m,g,root=root)
write('state/active_campaign.yml',m)
write('state/next_round_plan.yml',dict(round_index=225,status='active',campaign_id=cid,starting_graph_sha256=h,predecessor_round=224,tasks=[t['id'] for t in tasks]))
lp=Path('state/round_ledger.yml');s=lp.read_text(encoding='utf-8');ledger=json.loads(s)
assert ledger['rounds'][-1]['round_index']==224 and ledger['rounds'][-1]['status']=='closed'
entry=dict(round_index=225,campaign_id=cid,type=m['round_type'],status='active',objective=m['frozen_target']['question'],
 tasks=[{k:t[k] for k in ['id','role','status']} for t in tasks],resource_policy=m['resource_policy'],
 starting_graph_sha256=h,exit_labels=m['exit_labels'],started_at=now)
marker='\n  ]\n}';head,tail=s.rsplit(marker,1)
new=head+',\n'+'\n'.join('    '+line for line in json.dumps(entry,indent=2).splitlines())+marker+tail
new=new.replace('"active_round": 224','"active_round": 225',1)
ledger['active_round']=225;ledger['rounds'].append(entry);assert json.loads(new)==ledger;put(lp,new.encode())
matrix=read('state/validation_matrix.yml')
matrix.update(campaign_id=cid,promotion_status='round_225_active_no_promotion',graph_sha256=h,
 decision_rule='Complete actual nonlinear circle wave; exact arithmetic factorization is not a new bound.')
for t in tasks:matrix['gates'].append(dict(id='round225_'+t['id'],status='pending',artifact=t['report_path']))
matrix['gates'].append(dict(id='round225_conductor_reconciliation',status='pending',artifact=base.as_posix()+'/reviews/conductor_round225_reconciliation.md'))
write('state/validation_matrix.yml',matrix)
write(base/'controls/starting_state_hashes.json',{p:sha(p) for p in ['state/proof_obligations.yml','state/best_proof_draft.md','strategy/gauss_circle_strategy_review_2026-09-23.md']})
failure=Path('state/failure_ledger.md');oldbytes=failure.read_bytes()
prepare_campaign(m,g,root=root,graph_path=root/'state/proof_obligations.yml')
put(failure,oldbytes+b'\n\n## Round225 complete logarithmic-convolution barriers\n\nThe complete actual circle wave uses r2, not the GAR angular coefficient. Prime-factorization identities do not save powers. Keep both Lambda and chi4 Lambda branches, every prime power, n=1, literal U/V endpoints, all Type-I/II complements and the nonlinear real phase. Do not import linear multiplicative theorems or fixed-class assumptions from223 without a proved bridge. All actual vector norms, product masks and infinite Schwartz tails must be restored before comparing with beta=2theta_LY-1/2. The completed-row Hecke self-return224 and expanded/incidence/grouped certificate floors do not lower-bound the signed wave. Full quarter remains open; next mandatory broad review226.\n')
write(base/'controls/frozen_artifact_hashes.json',{p.as_posix():sha(p) for p in [base/'plan.json',Path(strategy)]+sorted((base/'briefs').glob('*.md'))})
for t in m['tasks']:t['status']='running'
write('state/active_campaign.yml',m);assert not validate_campaign(m,g,root=root)
write(base/'controls/dispatch_provenance.json',dict(round_index=225,frozen_objective_changed=False,
 agent_reuse={'complete_nonlinear_prime_attack':'/root/full_frontier_sources','complete_factor_norm_audit':'/root/joint_divisor_kernel','blind_finite_convolution':'/root/joint_lattice_kernel'},
 isolation='Blind task reads only protocol and isolated packet; reused history disclosed. Other tasks use named context and cannot read current siblings.',
 previous_turn_classification=m['previous_goal_turn_classification'],mathematical_numerical_experiments=0))
print('Round225 frozen; all635 previous archive entries checked; graph401 unchanged; three bounded tasks ready.')
