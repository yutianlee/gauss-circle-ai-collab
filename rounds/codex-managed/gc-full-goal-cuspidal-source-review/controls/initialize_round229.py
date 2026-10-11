"""Freeze229 after verified closed228. Never rerun after success."""
import hashlib,json,sys
from pathlib import Path
from datetime import datetime,timezone
root=Path.cwd();sys.path.insert(0,str(root))
from math_collab.campaigns import validate_campaign,prepare_campaign
from math_collab.proof_obligations import load_graph,validate_graph
cid='gc-full-goal-cuspidal-source-review';base=Path('rounds/codex-managed')/cid
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def write(p,o):Path(p).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
old=read('state/active_campaign.yml');assert old['round_index']==228 and old['status']=='complete'
assert not (base/'plan.json').exists()
entries=[e for e in read('state/round_ledger.yml')['rounds'] if 200<=e['round_index']<=228]
assert len(entries)==29 and all(e['status']=='closed' for e in entries)
count=0
for e in entries:
 for p,h in read(Path('rounds/codex-managed')/e['campaign_id']/'controls/artifact_hashes.json').items():
  assert sha(p)==h,p;count+=1
assert count==763
g=load_graph(Path('state/proof_obligations.yml'));assert len(g['proof_obligations'])==401 and not validate_graph(g,root=root)
h=sha('state/proof_obligations.yml');assert h==old['closing_assessment']['resulting_graph_sha256']
strategy='strategy/round229_full_goal_cuspidal_source_review.md';now=datetime.now(timezone.utc).isoformat()
for d in ['briefs','reports','reviews','candidates','controls']:(base/d).mkdir(parents=True,exist_ok=True)
prev='rounds/codex-managed/gc-signed-heegner-phase/'
common=['protocol.md','state/proof_obligations.yml','state/active_campaign.yml',strategy,
'strategy/gauss_circle_strategy_review_2026-09-23.md',
'strategy/gauss_circle_strategy_checkpoint_round226_2026-09-28.md',
base.as_posix()+'/briefs/complete_cuspidal_interfaces.md',prev+'synthesis.md',
'proofs/kernels/gc_complete_square_root_large_values_moment_bound.md']
specs=[
('signed_cm_spectral_sources','source_auditor','selected_context',
'Bounded current-primary audit of the COMPLETE actual CM-weighted signed cusp sum. At most TWO exact theorem audits after bounded screening. Investigate a lawful CM point-value/central-L-value formula and a genuinely signed spectral, relative-trace, Kuznetsov or reciprocity estimate that could see the actual surviving phase (qdR^2/n)^(it). Match conductors1 and2, even/Fricke-plus, oldspace denominator, harmonic and area weights, local two-factors and all moving test functions. The entire continuous partner is reviewed target-sized but must remain in reconstruction. Sources must state exact versions, theorem numbers, hypotheses and quantitative height/derivative/strip costs. A fixed-coefficient or averaged-point theorem does not automatically control the actual fixed CM test. Derive all approximate-functional-equation lengths and norms if used; preserve every discrete mode, descendant, dual tail and geometric term. Compare the full restored raw size with A^2N^(3/2) and the original A^2N^2 cap. Repeating the228 positive price or formal inversion is not a new mechanism. Recommend one COMPLETE quantitative next objective with a concrete new input, or a precise first failed import premise. Seven numbered sections, no experiments, no current siblings/blind/root controls, assigned report only, final SHA256 and stop.',
common+[prev+'reports/signed_hecke_functional_attack.md',prev+'reviews/independent_signed_hecke_review.md',prev+'reports/complete_eisenstein_pairing.md',prev+'reviews/independent_eisenstein_review.md','rounds/codex-managed/gc-complete-joint-spectral-remainder/reports/heegner_joint_norm_audit.md']),
('complete_frontier_source_comparison','source_auditor','selected_context',
'Independent mandatory current-primary review of alternative COMPLETE full-proof frontiers after226--228. At most TWO exact theorem audits after bounded screening. Seek source-compatible new harmonic/Fourier/decoupling, high-moment, arithmetic correlation or complete bilinear input, and compare with the now entirely paid continuous spectrum plus remaining ENTIRE cusp owner. Preserve all M1 HARD/SMOOTH, M2 TOP/BAL/UNBAL, GAR lower/cross owners and endpoints; retain complete real versus complex scope and adequate unbounded FIXED even-order family. Do not extrapolate an unweighted fourth moment, rational-time, averaged-radius, random/distributional, prime-only or local-sector theorem to the full objective. Exact paper version/date/theorem/hypotheses and all coefficient, transform, norm, endpoint and complement costs are required. Use the named existing barriers to avoid repeating retired positive transfers. Recommend one quantitatively specified complete next objective with an identifiable new reason, or clearly identify why the tested import does not improve a full bound. No broad catalog without application audit, no numerical experiments, no current sibling/blind/root-control reads. Seven numbered sections, assigned report only, freeze final SHA256 and stop.',
common+['state/best_proof_draft.md','proofs/kernels/gc_complete_distinct_radical_moment_reduction.md','rounds/codex-managed/gc-full-goal-spectral-source-review/reports/theta_wave_full_frontiers.md','rounds/codex-managed/gc-complete-logarithmic-convolution/synthesis.md','rounds/codex-managed/gc-full-goal-signed-source-review/reports/geometric_complete_frontiers.md']),
('blind_radial_abel_kernel','blind_rederiver','statement_only',
'Read ONLY protocol.md and the isolated radial Abel statement. Derive or refute the exact transform, support, uniform front profile, sharp complete absolute radial mass and signed mass. Pay the entire interior and r=0. Distinguish compact time from smooth compact spectral cutoff without unsupported automorphic assertions. No sources, experiments, arithmetic or other context. Seven numbered sections, only assigned report, disclose isolation, freeze SHA256 and stop.',
['protocol.md',base.as_posix()+'/briefs/blind_radial_abel_statement.md'])]
controls=['current_primary_versions','exact_source_hypotheses','actual_coefficients_and_cm_measure','growing_test_and_transform_costs','complete_cusp_and_continuous_ownership','all_shifts_endpoints_and_tails','complete_alternative_frontiers','real_complex_and_average_scope','full_power_restoration','certificate_not_actual_lower_bound','statement_only_control','fixed_unbounded_order_scope']
tasks=[]
for ident,role,mode,target,ctx in specs:
 t=dict(id=ident,role=role,access_mode=mode,status='pending',target=target,context_files=ctx,required_controls=controls,required_output=['Seven numbered protocol sections: result, hypotheses, proof/derivation, first gap, controls, exact provenance, state effect.','Assigned report only; primary source cards for imported theorems; final SHA256 then stop.'],report_path=base.as_posix()+'/reports/'+ident+'.md')
 if mode=='statement_only':t['excluded_context']=['All except protocol and isolated statement; no arithmetic/source/history context.']
 tasks.append(t)
m=dict(schema_version=1,round_index=229,round_type='mandatory_full_goal_cuspidal_source_review',campaign_id=cid,title='Full-goal cuspidal, wave and moment strategy review',status='active',max_concurrency=3,coordinator='Codex',starting_graph_sha256=h,generated_at=now,
resource_policy=dict(analytical_algebraic_minimum_percent=95,numerical_experimental_maximum_percent=5,planned_numerical_percent=0,budget='Three bounded reports; at most two exact theorem audits per source role, one review/repair cycle, zero experiments.'),
target_obligations=['GC-target','M9-M1','M9-M2','GC-complete-square-root-large-values-moment-bound','GC-complete-distinct-radical-twelfth-reduction'],
frozen_target=dict(question='Which current exactly applicable signed cuspidal or alternative full-frontier method can advance the FULL quarter goal after226--228, and what complete next inequality is justified?',reference_formula='Full P(X)<<X^(1/4+epsilon); exact whole cusp target2Re D<=A_J^2N^(3/2)T^epsilon with entire continuous component already reviewed; every complete alternative remains in scope.',quantities=['Actual r2, CM measures, primitive local factors, every real radius, shift, scale, spectral channel, endpoint and tail.','Inherited beta is only complete real; fixed twelfth29/25 implies102/325 only.','A shorter dual transform or paid complete component is not a complete-wave gain.','Wave-kernel absolute mass and actual signed arithmetic cancellation are distinct.']),
completion_criteria=['Two bounded current-primary and full-frontier reports plus one isolated radial Abel derivation.','Final-hash nonauthor source/application and scalar-control reviews, conductor strategy checkpoint and complete restoration.','Validated complete gain or explicit no-gain synthesis and mechanically valid State Patch before230 design.'],
controls=controls,exit_labels=['complete_cuspidal_source_gain_requires_validation','strategy_cuspidal_source_review_no_complete_gain'],tasks=tasks,
review_seams=[dict(id='actual_cm_signed_source',requirement='Source versions, exact CM harmonic measure, primitive/local factors and growing spectral tests.'),dict(id='radial_abel_control',requirement='Isolated full mass/profile derivation and separate nonauthor application review.'),dict(id='complete_frontier_strategy',requirement='All complete owners, current benchmark status, full costs and one next quantitative inequality.')],
previous_goal_turn_classification='progress_reviewed_complete_continuous_component_and_cusp_reduction_no_complete_wave_gain',
scheduled_review='Mandatory229 after226--228; next broad strategy/current-primary review232.')
assert not validate_campaign(m,g,root=root)
write('state/active_campaign.yml',m)
write('state/next_round_plan.yml',dict(round_index=229,status='active',campaign_id=cid,starting_graph_sha256=h,predecessor_round=228,tasks=[t['id'] for t in tasks]))
lp=Path('state/round_ledger.yml');s=lp.read_text(encoding='utf-8');ledger=json.loads(s)
assert ledger['rounds'][-1]['round_index']==228 and ledger['rounds'][-1]['status']=='closed'
entry=dict(round_index=229,campaign_id=cid,type=m['round_type'],status='active',objective=m['frozen_target']['question'],tasks=[{k:t[k] for k in ['id','role','status']} for t in tasks],resource_policy=m['resource_policy'],starting_graph_sha256=h,exit_labels=m['exit_labels'],started_at=now)
marker='\n  ]\n}';head,tail=s.rsplit(marker,1)
new=head+',\n'+'\n'.join('    '+line for line in json.dumps(entry,indent=2).splitlines())+marker+tail
new=new.replace('"active_round": 228','"active_round": 229',1)
ledger['active_round']=229;ledger['rounds'].append(entry);assert json.loads(new)==ledger;lp.write_bytes(new.encode())
matrix=read('state/validation_matrix.yml');matrix.update(campaign_id=cid,promotion_status='round_229_active_no_promotion',graph_sha256=h,decision_rule='Current full-goal source review; no source theorem or cancellation estimate accepted at launch.')
for t in tasks:matrix['gates'].append(dict(id='round229_'+t['id'],status='pending',artifact=t['report_path']))
matrix['gates'].append(dict(id='round229_conductor_reconciliation',status='pending',artifact=base.as_posix()+'/reviews/conductor_round229_reconciliation.md'))
write('state/validation_matrix.yml',matrix)
write(base/'controls/starting_state_hashes.json',{p:sha(p) for p in ['state/proof_obligations.yml','state/best_proof_draft.md','strategy/gauss_circle_strategy_review_2026-09-23.md']})
failure=Path('state/failure_ledger.md');oldbytes=failure.read_bytes()
prepare_campaign(m,g,root=root,graph_path=root/'state/proof_obligations.yml')
failure.write_bytes(oldbytes+b'\n\n## Round229 full-goal cuspidal source barriers\n\nAll763 archived entries from200--228 verified. Round228 reviewed the entire continuous component at target size, but no full-wave gain. The complete cusp owner retains all primitive levels, oldspace weights, two-adic factors and spectral phases. Formal inversion and the shorter qt/L dual vector alone do not estimate cancellation. Source imports must pay actual CM harmonic measure, growing tests, strip and separation costs, every geometric and spectral partner, and reconstruction. Keep all alternative M1/M2/GAR/endpoints and unbounded fixed-order moment owners. No source resemblance, averaged surrogate or unestimated complement is a complete advance.\n')
write(base/'controls/frozen_artifact_hashes.json',{p.as_posix():sha(p) for p in [base/'plan.json',Path(strategy)]+sorted((base/'briefs').glob('*.md'))})
for t in m['tasks']:t['status']='running'
write('state/active_campaign.yml',m);assert not validate_campaign(m,g,root=root)
write(base/'controls/dispatch_provenance.json',dict(round_index=229,frozen_objective_changed=False,agent_tasks=[t['id'] for t in tasks],isolation='Three fresh fork_none roles. Blind initial input only protocol and isolated statement; no sibling reads before freeze.',previous_turn_classification=m['previous_goal_turn_classification'],mathematical_numerical_experiments=0))
print('Round229 frozen; all763 prior archive entries verified; graph401 unchanged.')
