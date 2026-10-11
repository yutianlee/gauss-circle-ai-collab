"""Freeze226 after verified closed225. Never rerun after success."""
import hashlib,json,sys
from pathlib import Path
from datetime import datetime,timezone
root=Path.cwd();sys.path.insert(0,str(root))
from math_collab.campaigns import validate_campaign,prepare_campaign
from math_collab.proof_obligations import load_graph,validate_graph
cid='gc-full-goal-spectral-source-review';base=Path('rounds/codex-managed')/cid
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def write(p,o):Path(p).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
old=read('state/active_campaign.yml');assert old['round_index']==225 and old['status']=='complete'
assert not (base/'plan.json').exists()
entries=[e for e in read('state/round_ledger.yml')['rounds'] if 200<=e['round_index']<=225]
assert len(entries)==26 and all(e['status']=='closed' for e in entries)
count=0
for e in entries:
 for p,h in read(Path('rounds/codex-managed')/e['campaign_id']/'controls/artifact_hashes.json').items():
  assert sha(p)==h,p;count+=1
assert count==667
g=load_graph(Path('state/proof_obligations.yml'));assert len(g['proof_obligations'])==401 and not validate_graph(g,root=root)
h=sha('state/proof_obligations.yml');assert h==old['closing_assessment']['resulting_graph_sha256']
strategy='strategy/round226_full_goal_spectral_source_review.md';now=datetime.now(timezone.utc).isoformat()
for d in ['briefs','reports','reviews','candidates','controls']:(base/d).mkdir(parents=True,exist_ok=True)
common=['protocol.md','state/proof_obligations.yml','state/active_campaign.yml',strategy,
'strategy/gauss_circle_strategy_review_2026-09-23.md',
'strategy/gauss_circle_strategy_checkpoint_round223_2026-09-28.md',
base.as_posix()+'/briefs/conductor_complete_spectral_interfaces.md',
'rounds/codex-managed/gc-complete-logarithmic-convolution/synthesis.md',
'rounds/codex-managed/m9-m1-complete-gar-prime-amplification/synthesis.md',
'proofs/kernels/gc_complete_square_root_large_values_moment_bound.md']
specs=[
('actual_shifted_spectral_sources','source_auditor','selected_context',
'Bounded current-primary audit of actual r2(n+h)r2(n) spectral/shifted-convolution estimates, at most TWO exact theorem audits. Start from Hulse-Kuan-Lowry-Duda-Walker arXiv1705.04771 and inspect its current exact primary theorem text, shift dependence, smoothed versus sharp error, spectral exceptional terms and test-function dependence. Screen a distinct current extension only if source-compatible. Map the actual nonlinear C_h(R) packet, with R~T, growing shifts and all overlapping endpoints; price every derivative or Mellin/contour norm, main term, error and all shifts. Compare full restored wave/moment costs, not a small zero mode. Round221 already priced elementary divisor completion; do not repeat it or use withdrawn Kim2509.24152. No cusp, function-field or fixed-h substitution without proof. Recommend ONE complete quantified next inequality with a reason to expect genuinely new arithmetic input, or a precise first failed premise. Full quarter and unbounded fixed-order scope preserved. Seven sections, exact primary URLs/versions/theorem numbers, zero experiments; assigned report only, no siblings/shared edits/successor, stop at final hash.',
common+['rounds/codex-managed/gc-actual-vector-gram-correlations/synthesis.md','rounds/codex-managed/gc-actual-vector-gram-correlations/reports/actual_shifted_correlations.md','proofs/kernels/gc_complete_distinct_radical_moment_reduction.md']),
('theta_wave_full_frontiers','source_auditor','selected_context',
'Independent bounded current-primary theta/automorphic-wave/harmonic-analysis source review and COMPLETE frontier comparison, at most TWO exact theorem audits. Seek a theorem retaining the actual oscillatory phase beyond the225 multiplicative norm closure and the223 absolute chirp transfer. Theta modularity, complex heat/subordination, metaplectic/spectral wave or decoupling are possible leads, not mandatory imports. Require exact actual r2 or GAR coefficient match; cusp-only, averaged-radius, random/distributional, rational-time, smooth-number and almost-everywhere results do not give the required uniform full theorem without proved transfers. Price damping removal, contour/transform norms, major/minor/rational regimes, exceptional terms and all scales. Compare M1 HARD/SMOOTH, M2 TOP/BAL/UNBAL, GAR and moment alternatives using graph and223 checkpoint; do not drop an owner. Screen current primary records then audit only source-compatible statements; exact identities alone not gain. Recommend one COMPLETE next objective with a specific actual signed mechanism. Seven sections, exact primary links/versions/theorem hypotheses, zero experiments; no sibling/blind/shared/successor work, report and stop.',
common+['state/best_proof_draft.md','rounds/codex-managed/gc-full-goal-signed-source-review/reports/multiplicative_wave_sources.md','rounds/codex-managed/gc-full-goal-signed-source-review/reports/geometric_complete_frontiers.md','strategy/gauss_circle_strategy_checkpoint_round211_2026-09-28.md']),
('blind_complex_subordination','blind_rederiver','statement_only',
'Read ONLY protocol and isolated packet. Independently derive/refute complex-subordination sectors, exact ray integral multiplier and optimal order in the stated range, including one-coefficient and sector-boundary controls. Seven sections, retained-history disclosure, no web/experiments or application. Assigned report only, no siblings/shared edits/successor; stop at final hash.',
['protocol.md',base.as_posix()+'/briefs/blind_complex_subordination_statement.md'])]
controls=['current_primary_versions','exact_source_hypotheses','actual_coefficients_and_phase','growing_parameter_uniformity','spectral_and_contour_costs','complete_frontiers','all_shifts_endpoints_and_tails','real_complex_and_average_scope','full_power_restoration','actual_vs_certificate_scope','statement_only_control','fixed_unbounded_order_scope']
tasks=[]
for ident,role,mode,target,ctx in specs:
 t=dict(id=ident,role=role,access_mode=mode,status='pending',target=target,context_files=ctx,required_controls=controls,required_output=['Seven numbered protocol sections: result, exact hypotheses, derivation, first gap, controls, dependencies/provenance, recommended state effect.','Only assigned report; exact primary URLs/versions/theorem numbers for external claims. Stop after final SHA256.'],report_path=base.as_posix()+'/reports/'+ident+'.md')
 if mode=='statement_only':t['excluded_context']=['All except protocol and isolated statement; prior history disclosed.']
 tasks.append(t)
m=dict(schema_version=1,round_index=226,round_type='mandatory_full_goal_spectral_source_review',campaign_id=cid,title='Full-goal spectral, shifted-convolution and theta source review',status='active',max_concurrency=3,coordinator='Codex',starting_graph_sha256=h,generated_at=now,
resource_policy=dict(analytical_algebraic_minimum_percent=95,numerical_experimental_maximum_percent=5,planned_numerical_percent=0,budget='Three bounded reports, at most two exact theorem audits per source role, one review/repair cycle, zero experiments.'),
target_obligations=['GC-target','M9-M1','M9-M2','GC-complete-square-root-large-values-moment-bound','GC-complete-distinct-radical-twelfth-reduction'],
frozen_target=dict(question='Can a current exactly applicable spectral, shifted-convolution or theta/wave source advance a complete full-proof frontier after223--225, and what complete next estimate is justified?',reference_formula='Full P(X)<<X^(1/4+epsilon); complete actual real B_T(R)<<T^epsilon, all M1/M2/GAR/endpoints or a sufficient unbounded fixed-order moment family. Local factor or transform identities are not gains.',quantities=['Every real radius, actual coefficients, all shifts, parameter dependence, exceptional spectra, masks, endpoints and tails.','Inherited beta is only complete real; fixed twelfth29/25 is only102/325.','Existing223 chirp,224 angular commutator,225 all-scale81/614 and221 alias costs remain scoped evidence.','Complex contour identity and its absolute transfer norm are different from an actual oscillatory lower bound.']),
completion_criteria=['Two bounded current-primary and complete-frontier reports plus isolated subordination derivation.','Independent final-hash source/application and control reviews, strategy checkpoint and exact full costs.','Validated complete gain or explicit no-gain synthesis and State Patch; close226 before successor227.'],
controls=controls,exit_labels=['complete_spectral_source_gain_requires_validation','strategy_spectral_source_review_no_complete_gain'],tasks=tasks,
review_seams=[dict(id='actual_spectral_application',requirement='Source versions, r2 coefficients, growing shifts and test-function/spectral costs.'),dict(id='complex_subordination',requirement='Statement-only sector/constant/norm proof and independent application review.'),dict(id='full_goal_strategy',requirement='All complete owners, benchmark status, quantitative next inequality and full quarter scope.')],
previous_goal_turn_classification='progress_completed_reviewed_round_changes_method_selection_no_complete_analytic_gain',
scheduled_review='Mandatory226 after223--225; next broad strategy/current-primary review229.')
assert not validate_campaign(m,g,root=root)
write('state/active_campaign.yml',m)
write('state/next_round_plan.yml',dict(round_index=226,status='active',campaign_id=cid,starting_graph_sha256=h,predecessor_round=225,tasks=[t['id'] for t in tasks]))
lp=Path('state/round_ledger.yml');s=lp.read_text(encoding='utf-8');ledger=json.loads(s)
assert ledger['rounds'][-1]['round_index']==225 and ledger['rounds'][-1]['status']=='closed'
entry=dict(round_index=226,campaign_id=cid,type=m['round_type'],status='active',objective=m['frozen_target']['question'],tasks=[{k:t[k] for k in ['id','role','status']} for t in tasks],resource_policy=m['resource_policy'],starting_graph_sha256=h,exit_labels=m['exit_labels'],started_at=now)
marker='\n  ]\n}';head,tail=s.rsplit(marker,1)
new=head+',\n'+'\n'.join('    '+line for line in json.dumps(entry,indent=2).splitlines())+marker+tail
new=new.replace('"active_round": 225','"active_round": 226',1)
ledger['active_round']=226;ledger['rounds'].append(entry);assert json.loads(new)==ledger;lp.write_bytes(new.encode())
matrix=read('state/validation_matrix.yml');matrix.update(campaign_id=cid,promotion_status='round_226_active_no_promotion',graph_sha256=h,decision_rule='Complete source review; no source or cancellation theorem accepted at launch.')
for t in tasks:matrix['gates'].append(dict(id='round226_'+t['id'],status='pending',artifact=t['report_path']))
matrix['gates'].append(dict(id='round226_conductor_reconciliation',status='pending',artifact=base.as_posix()+'/reviews/conductor_round226_reconciliation.md'))
write('state/validation_matrix.yml',matrix)
write(base/'controls/starting_state_hashes.json',{p:sha(p) for p in ['state/proof_obligations.yml','state/best_proof_draft.md','strategy/gauss_circle_strategy_review_2026-09-23.md']})
failure=Path('state/failure_ledger.md');oldbytes=failure.read_bytes()
prepare_campaign(m,g,root=root,graph_path=root/'state/proof_obligations.yml')
failure.write_bytes(oldbytes+b'\n\n## Round226 full-goal spectral source barriers\n\nAll667 prior archived entries verified. Round225 completes a bounded reviewed attempt but no analytic exponent gain. Keep223 source/absolute-transfer limits,224 actual angular commutator and225 all-scale factor costs. Round221 already prices elementary shifted r2 aliases: source review must supply new uniform oscillatory information, not repeat a small main mode. Growing shifts, oscillatory-test derivatives, exceptional spectra and complex contour limits cannot be suppressed. Compare every complete owner and retain the full quarter target. No source resemblance, transform identity or unestimated complement is progress.\n')
write(base/'controls/frozen_artifact_hashes.json',{p.as_posix():sha(p) for p in [base/'plan.json',Path(strategy)]+sorted((base/'briefs').glob('*.md'))})
for t in m['tasks']:t['status']='running'
write('state/active_campaign.yml',m);assert not validate_campaign(m,g,root=root)
write(base/'controls/dispatch_provenance.json',dict(round_index=226,frozen_objective_changed=False,agent_reuse={'actual_shifted_spectral_sources':'/root/full_frontier_sources','theta_wave_full_frontiers':'/root/joint_divisor_kernel','blind_complex_subordination':'/root/joint_lattice_kernel'},isolation='Blind reads protocol and isolated packet only; retained history disclosed. Others use named context, no siblings.',previous_turn_classification=m['previous_goal_turn_classification'],mathematical_numerical_experiments=0))
print('Round226 frozen; all667 prior archive entries verified; graph401 unchanged.')
