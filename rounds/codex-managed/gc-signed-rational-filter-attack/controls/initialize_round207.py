"""Freeze207 after the closed206 evidence; no mathematical mutation."""
import copy, hashlib, json, sys
from datetime import datetime, timezone
from pathlib import Path
root=Path.cwd(); sys.path.insert(0,str(root))
from math_collab.campaigns import validate_campaign, prepare_campaign
from math_collab.proof_obligations import load_graph, validate_graph
cid='gc-signed-rational-filter-attack'; base=Path('rounds/codex-managed')/cid
for d in ['briefs','reports','candidates','reviews','controls']:(base/d).mkdir(parents=True,exist_ok=True)
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def write(p,o):Path(p).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
old=read('state/active_campaign.yml'); assert old['round_index']==206 and old['status']=='complete'
prior='rounds/codex-managed/gc-complete-signed-shell-arithmetic'
for p,h in read(f'{prior}/controls/artifact_hashes.json').items():assert sha(p)==h,p
g=load_graph(Path('state/proof_obligations.yml')); assert not validate_graph(g,root=root)
h=sha('state/proof_obligations.yml'); assert h==old['starting_graph_sha256']
nodes={n['id']:n for n in g['proof_obligations']}; assert nodes['GC-target']['status']=='open'
now=datetime.now(timezone.utc).isoformat(); strategy='strategy/round207_signed_rational_filter_attack.md'
common=['protocol.md','state/proof_obligations.yml','state/active_campaign.yml',strategy,
 f'{prior}/reports/actual_divisor_shell_attack.md',f'{prior}/controls/conductor_sixth_moment_power_ledger.md',
 f'{prior}/reviews/independent_divisor_obstruction_review.md',f'{prior}/reviews/independent_bridge_power_review.md',
 'rounds/codex-managed/gc-full-frontier-moment-strategy-review/controls/conductor_middle_band_strategy.md',
 'proofs/kernels/gc_complete_square_root_large_values_moment_bound.md']
controls=['complete_middle_range','actual_two_arm_characters','all_harmonics_and_duplicates',
 'moving_threshold_error','low_period_annihilation','variable_width','real_endpoints_and_tails',
 'signed_not_positive','restored_sixth_and_twelfth_powers','source_hypotheses','full_proof_scope']
specs=[
 ('periodic_hyperbola_attack','discovery','selected_context',
  'Derive the complete actual-r2 band-filtered hyperbola formula, freeze moving thresholds only with a proved error, evaluate exact mod4 Gauss factors and short-period annihilation, retain both arms and all coincident rational frequencies. Then attempt a signed sixth estimate beyond rewriting the identity. Price the complete result against T^(129/25-6omega); preserve every middle N. At least one real signed-sum estimate or an actual-coefficient norm-placement obstruction is required. No successor design or broad literature survey.',common),
 ('signed_rational_moment_attack','discovery','selected_context',
  'Independently derive enough of the complete actual hyperbola/rational formula to attack its sixth correlation or a genuine bilinear/reciprocal-phase estimate. Keep both arms, all characters and mod4 phases, variable width, masks and boundary error. Price physical coefficient norms, frequency collisions, all shifts and reconstruction. Inspect at most two substantive primary theorem interfaces if useful; every hypothesis and net power must match. Do not repeat pair variance or positive six-shift counting as a gain. Produce a complete bound or a precise scoped obstruction to the attempted signed estimate, then stop.',common+['strategy/gauss_circle_strategy_review_2026-09-23.md']),
 ('blind_periodic_threshold','blind_rederiver','statement_only',
  'Prove or refute the periodic Poisson, exact mod4 phase and threshold-freezing assertions of the isolated packet. Preserve real endpoints and variable widths; no claimant context. Stop after the assigned seven-section report.',
  ['protocol.md',f'{base.as_posix()}/briefs/blind_periodic_threshold_statement.md'])]
tasks=[]
for ident,role,mode,target,context in specs:
 t=dict(id=ident,role=role,access_mode=mode,status='pending',target=target,context_files=context,
  required_controls=controls,required_output=['Seven numbered sections: result, exact hypotheses, proof, first gap, controls, exact dependencies, state effect.',
  'Write only the assigned report. No graph, proof draft, validation matrix, synthesis, source-card or successor edits.'],
  report_path=f'{base.as_posix()}/reports/{ident}.md')
 if mode=='statement_only':t['excluded_context']=['Graph, campaign, general brief, strategy, predecessors, claimants, siblings and web.']
 tasks.append(t)
m=dict(schema_version=1,round_index=207,round_type='complete_signed_rational_moment_attack',campaign_id=cid,
 title='Complete signed rational-filter arithmetic moment attack',status='active',max_concurrency=3,coordinator='Codex',
 starting_graph_sha256=h,generated_at=now,
 resource_policy=dict(analytical_algebraic_minimum_percent=100,numerical_experimental_maximum_percent=0,planned_numerical_percent=0,
 budget='Three bounded analytical/source reports, conductor signed-norm analysis, one same-round seam cycle. No mathematical numerical experiments.'),
 target_obligations=['GC-target','GC-complete-square-root-large-values-moment-bound'],
 frozen_target=dict(question='Can the complete actual signed rational-filter representation yield the required middle-band moment saving?',
 reference_formula='Integral_I |sum_(T^(52/125)<N=2^j<T^(99/125)) S_N|^12 << T^(29/25+epsilon); sufficient K6(N)<<T^(129/25-6omega(alpha)+epsilon).',
 quantities=['I=[T/sqrt(2),sqrt(3)T], X=T^2, h(x)=2sqrt(x)/sqrt(N), exact fixed205 filters.',
 'omega=min(alpha/4,beta,(1-alpha)/2); sixth saving still needed g=6omega-4/25-29alpha/110.',
 'All outer bands are already estimated; best complete p12 remains10beta; milestone would imply only102/325.']),
 completion_criteria=['Three seven-section reports, including statement-only rederivation of an important threshold/filter lemma.',
 'Complete actual arithmetic estimate attempted after the transform, or a proved actual-coefficient norm-placement obstruction.',
 'Both hyperbola arms, all frequencies, masks, errors, real endpoints and full middle range retained.',
 'Exact independent seams and source cards for promotion; otherwise identity patch.',
 'Conductor synthesis, mechanically validated State Patch, and closed ledger before208.'],
 controls=controls,exit_labels=['complete_signed_arithmetic_gain','complete_rational_attempt_no_gain','scoped_rational_method_no_go'],tasks=tasks,
 review_seams=[dict(id='periodic_threshold',requirement='Exact Gauss factors, periodic cancellation, threshold and tail errors.'),
 dict(id='signed_moment',requirement='Complete actual coefficient correlation, restored norm powers and scope.')],
 previous_goal_turn_classification='progress_scoped_method_no_go_and_validated_evidence_changed_next_action_no_complete_bound_gain',
 scheduled_review='Mandatory broad strategy/current-literature review208 after205--207.')
assert not validate_campaign(m,g,root=root)
write('state/active_campaign.yml',m)
write('state/next_round_plan.yml',dict(round_index=207,status='active',campaign_id=cid,starting_graph_sha256=h,
 predecessor_round=206,design_choice=m['frozen_target']['question'],tasks=[t['id'] for t in tasks]))
lp=Path('state/round_ledger.yml'); raw=lp.read_bytes(); s=raw.decode('utf-8'); ledger=json.loads(s)
assert ledger['rounds'][-1]['round_index']==206 and ledger['rounds'][-1]['status']=='closed'
entry=dict(round_index=207,campaign_id=cid,type=m['round_type'],status='active',objective=m['frozen_target']['question'],
 tasks=[{k:t[k] for k in ['id','role','status']} for t in tasks],resource_policy=m['resource_policy'],starting_graph_sha256=h,
 exit_labels=m['exit_labels'],started_at=now)
eol='\r\n' if '\r\n' in s else '\n'; marker=eol+'  ]'+eol+'}'
head,tail=s.rsplit(marker,1); new=head+','+eol+eol.join('    '+line for line in json.dumps(entry,indent=2).splitlines())+marker+tail
new=new.replace('"active_round": 206','"active_round": 207',1)
ledger['active_round']=207;ledger['rounds'].append(entry);assert json.loads(new)==ledger
lp.write_bytes(new.encode('utf-8'))
matrix=read('state/validation_matrix.yml');matrix.update(campaign_id=cid,promotion_status='round_207_active_no_promotion',graph_sha256=h,
 decision_rule='Complete signed rational-filter attempt; no new claim accepted at launch.')
for t in tasks:matrix['gates'].append(dict(id='round207_'+t['id'],status='pending',artifact=t['report_path']))
matrix['gates'].append(dict(id='round207_conductor_reconciliation',status='pending',artifact=f'{base.as_posix()}/reviews/conductor_round207_reconciliation.md'))
write('state/validation_matrix.yml',matrix)
write(base/'controls/starting_state_hashes.json',{p:sha(p) for p in ['state/proof_obligations.yml','state/best_proof_draft.md','strategy/gauss_circle_strategy_review_2026-09-23.md']})
# Prepare once. Preserve prior appended barrier evidence instead of deleting it.
failure=Path('state/failure_ledger.md'); failure_raw=failure.read_bytes()
prepare_campaign(m,g,root=root,graph_path=root/'state/proof_obligations.yml')
barrier='\n\n## Round207 frozen barriers\n\nRound206 proves that actual centered absolute sixth expansion is too large. Both hyperbola arms and the signed4--6-shift aggregate remain essential. Pair variance, discarded CRT errors, a Gaussian necessity inference and unestimated sub-bands are forbidden. This round tests short-period annihilation and fully paid threshold freezing before a complete signed rational estimate. See strategy/round207_signed_rational_filter_attack.md.\n'
failure.write_bytes(failure_raw+barrier.encode('utf-8'))
frozen_paths=[base/'plan.json',Path(strategy)]+sorted((base/'briefs').glob('*.md'))
write(base/'controls/frozen_artifact_hashes.json',{p.as_posix():sha(p) for p in frozen_paths})
for t in m['tasks']:t['status']='running'
write('state/active_campaign.yml',m)
assert not validate_campaign(m,g,root=root)
print('Round207 frozen, predecessor verified, three tasks ready; graph unchanged: '+h)
