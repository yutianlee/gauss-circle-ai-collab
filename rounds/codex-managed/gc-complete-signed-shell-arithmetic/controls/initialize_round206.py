"""Freeze Round206 only after verifying the closed205 evidence and graph."""
import copy, hashlib, json, sys
from datetime import datetime, timezone
from pathlib import Path
root=Path.cwd();sys.path.insert(0,str(root))
from math_collab.campaigns import validate_campaign
from math_collab.proof_obligations import load_graph, validate_graph
cid='gc-complete-signed-shell-arithmetic';base=Path('rounds/codex-managed')/cid
for d in ['briefs','reports','candidates','reviews','controls']:(base/d).mkdir(parents=True,exist_ok=True)
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def write(p,o):Path(p).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
old=read('state/active_campaign.yml');assert old['round_index']==205 and old['status']=='complete'
prior='rounds/codex-managed/gc-full-frontier-moment-strategy-review'
for p,h in read(f'{prior}/controls/artifact_hashes.json').items():assert sha(p)==h,p
g=load_graph(Path('state/proof_obligations.yml'));assert not validate_graph(g,root=root)
h=sha('state/proof_obligations.yml');assert h=='4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71'
nodes={n['id']:n for n in g['proof_obligations']}
assert nodes['GC-target']['status']=='open'
now=datetime.now(timezone.utc).isoformat();strategy='strategy/round206_complete_signed_shell_arithmetic_attack.md'
common=['protocol.md','state/proof_obligations.yml','state/active_campaign.yml',strategy,
        f'{prior}/controls/conductor_middle_band_strategy.md',f'{prior}/reviews/independent_middle_band_review.md',
        'proofs/kernels/gc_complete_square_root_large_values_moment_bound.md']
controls=['complete_middle_range','actual_r2_character','all_divisors_and_shifts','curvature_and_mean_error',
          'infinite_tails','real_endpoints','signed_not_positive','full_moment_power_ledger',
          'source_hypotheses','no_gaussian_inference','full_proof_scope']
specs=[
('actual_divisor_shell_attack','discovery','selected_context',
 'Attack the complete actual signed shell moment using r2=4 sum_(d|n)chi4(d). Derive a real arithmetic estimate beyond the already known Poisson identity and positive shell count. Attempt full coupled divisor or shifted correlations, keeping all divisors, repeated shifts, local congruence main terms, and errors. A possible sufficient sixth centered-filter moment is specified in the strategy, but it is unproved: derive and price its actual arithmetic expansion rather than assuming Gaussian behavior. A uniform estimate over every middle N suffices; no smaller unestimated complement. If the target fails to follow, give a complete bound and the exact first arithmetic inequality missing. No broad literature survey or successor design.',
 common+[f'{prior}/controls/conductor_arithmetic_source_gate.md',
 'rounds/codex-managed/gc-complete-signed-convolution-attack/reports/arithmetic_signed_tail_attack.md']),
('shifted_moment_source_attack','source_auditor','selected_context',
 'Audit and attempt actual-r2 short-interval sixth/higher-moment or shifted-spectral methods for the complete middle band. A candidate sufficient input is the centered additive-filter sixth moment at X h^3, h=2sqrt(x)/sqrt(N), X=T^2; test every transfer, filter, variable width, real endpoint and exceptional term. Inspect at most three substantive primary theorem interfaces, prioritizing actual representation-weight short-interval moments and shifted r2 correlations. Distinguish circle r2 from divisor d(n), indicator functions, random-model moments and zeta moments. Derive the strongest completely restored bound supplied by each serious legal import, or its first failed hypothesis; do not stop at a name list. A fourth/second moment is not a sixth moment. No source-card promotion, shared state or successor edits.',
 common+[f'{prior}/controls/conductor_arithmetic_source_gate.md',
 'strategy/gauss_circle_strategy_checkpoint_round205_2026-09-26.md']),
('blind_odd_shell_bridge','blind_rederiver','statement_only',
 'Independently prove or refute the curved-shell to centered additive-filter bridge, all errors, actual supremum and sixth-to-twelfth moment criterion in the isolated packet. No claimant context or external literature. Stop after the assigned report.',
 ['protocol.md',f'{base.as_posix()}/briefs/blind_odd_shell_statement.md'])]
tasks=[]
for ident,role,mode,target,context in specs:
 t=dict(id=ident,role=role,access_mode=mode,status='pending',target=target,context_files=context,required_controls=controls,
        required_output=['Seven numbered sections: result, exact hypotheses, proof, first gap, controls, exact dependencies, recommended state effect.',
                         'Write only the assigned report; no graph, draft, matrix, synthesis, source-card or successor edits.'],
        report_path=f'{base.as_posix()}/reports/{ident}.md')
 if mode=='statement_only':t['excluded_context']=['Graph, manifest, strategy, predecessor, claimant, siblings and external sources.']
 tasks.append(t)
m=dict(schema_version=1,round_index=206,round_type='complete_arithmetic_moment_attack',campaign_id=cid,
       title='Actual divisor and shifted-correlation attack on the complete signed shell moment',status='active',
       max_concurrency=3,coordinator='Codex',starting_graph_sha256=h,generated_at=now,
       resource_policy=dict(analytical_algebraic_minimum_percent=100,numerical_experimental_maximum_percent=0,
          planned_numerical_percent=0,budget='Three bounded analytical/source reports, conductor complete arithmetic analysis, one same-round seam cycle if needed. No mathematical numerical experiments.'),
       target_obligations=['GC-target','GC-complete-square-root-large-values-moment-bound'],
       frozen_target=dict(question='Can the actual signed middle-band shell moment gain the required complete power through arithmetic divisor or shifted-correlation information?',
          reference_formula='Integral_[T/sqrt(2),sqrt(3)T] |sum_(T^(52/125)<N=2^j<T^(99/125)) sum_m r2(m)m^(-1/4)L_(N,T)(R-sqrt(m))|^12 dR << T^(29/25+epsilon).',
          quantities=['L is the exact odd sine kernel and fixed smooth partition from the reviewed205 interface.',
                      'All other frequency ranges and all previous transform errors are already estimated.',
                      'Current full moment exponent10beta; required saving10beta-29/25; a success gives only102/325.']),
       completion_criteria=['Three seven-section reports including an isolated important-lemma rederivation.',
          'At least one complete actual arithmetic estimate attempted and priced beyond restating the transform.',
          'All middle scales, divisors, shifts, tails, exceptional sets and real endpoints retained.',
          'Exact independent seams and source checks for any accepted new theorem; otherwise identity patch.',
          'Graph-valid State Patch and conductor closure; full quarter goal and source qualifications retained.'],
       controls=controls,exit_labels=['complete_arithmetic_moment_gain','complete_arithmetic_attempt_no_gain','scoped_arithmetic_method_no_go'],
       tasks=tasks,review_seams=[dict(id='analytic_bridge',requirement='Exact filter/curvature/mean errors, supremum and moment normalization.'),
          dict(id='arithmetic_and_source',requirement='Actual coefficients, all coupled shifts and theorem hypotheses, complete restored power.')],
       previous_goal_turn_classification='progress_completed_review_and_evidence_changed_next_action_no_new_bound',
       scheduled_review='Next mandatory broad strategy/current-literature review208, after205--207.')
assert not validate_campaign(m,g,root=root)
write('state/active_campaign.yml',m)
write('state/next_round_plan.yml',dict(round_index=206,status='active',campaign_id=cid,starting_graph_sha256=h,
       predecessor_round=205,design_choice=m['frozen_target']['question'],tasks=[t['id'] for t in tasks]))
lp=Path('state/round_ledger.yml');raw=lp.read_bytes();s=raw.decode('utf-8');ledger=json.loads(s)
assert ledger['rounds'][-1]['round_index']==205 and ledger['rounds'][-1]['status']=='closed'
entry=dict(round_index=206,campaign_id=cid,type=m['round_type'],status='active',objective=m['frozen_target']['question'],
           tasks=[{k:t[k] for k in ['id','role','status']} for t in tasks],resource_policy=m['resource_policy'],
           starting_graph_sha256=h,exit_labels=m['exit_labels'],started_at=now)
eol='\r\n' if '\r\n' in s else '\n';marker=eol+'  ]'+eol+'}'
head,tail=s.rsplit(marker,1)
new=head+','+eol+eol.join('    '+line for line in json.dumps(entry,indent=2).splitlines())+marker+tail
new=new.replace('"active_round": 205','"active_round": 206',1)
ledger['active_round']=206;ledger['rounds'].append(entry);assert json.loads(new)==ledger
lp.write_bytes(new.encode('utf-8'))
matrix=read('state/validation_matrix.yml');matrix.update(campaign_id=cid,promotion_status='round_206_active_no_promotion',graph_sha256=h,
       decision_rule='Complete actual arithmetic moment attack; no new mathematical claim accepted at launch.')
for t in tasks:matrix['gates'].append(dict(id='round206_'+t['id'],status='pending',artifact=t['report_path']))
matrix['gates'].append(dict(id='round206_conductor_reconciliation',status='pending',artifact=f'{base.as_posix()}/reviews/conductor_round206_reconciliation.md'))
write('state/validation_matrix.yml',matrix)
write(base/'controls/starting_state_hashes.json',{p:sha(p) for p in ['state/proof_obligations.yml','state/best_proof_draft.md','strategy/gauss_circle_strategy_review_2026-09-23.md']})
print('Round206 frozen after verified205 closure; graph unchanged: '+h)
