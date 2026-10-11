"""Freeze one complete analytic objective and three independent interfaces."""
import json, hashlib
from pathlib import Path
from datetime import datetime, timezone

cid='gc-complete-signed-convolution-attack'
base=Path('rounds/codex-managed')/cid
for d in ['briefs','reports','candidates','reviews','controls']:(base/d).mkdir(parents=True,exist_ok=True)
def read(p):return json.loads(Path(p).read_text(encoding='utf-8'))
def write(p,o):Path(p).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
old=read('state/active_campaign.yml')
assert old['round_index']==202 and old['status']=='complete'
h=sha('state/proof_obligations.yml')
assert h=='abc88f6cd29d757b880037b6f600b802a22ac4b57fcce40662205150f3ed8ceb'
now=datetime.now(timezone.utc).isoformat()
strategy='strategy/round203_complete_signed_convolution_attack.md'
prior='rounds/codex-managed/gc-strategy-signed-moment-majorant-review'
common=['protocol.md','state/proof_obligations.yml','state/active_campaign.yml',strategy,f'{prior}/candidates/conductor_signed_convolution_interface.md',f'{prior}/reports/signed_cutoff_tail_moment_audit.md']
controls=['actual_coefficients','complete_tail_and_cross_terms','signed_filter_preserved','all_errors_priced','real_uniformity','net_exponent','independent_statement_only_control','no_parent_overclaim']
specs=[
('actual_density_remainder_attack','discovery','selected_context',
 'Attack the actual complete signed sixfold-convolution norm target via a continuous density subtraction. Derive a concrete density from the actual r_2 weights, use its oscillatory filtered cancellation, and rigorously estimate every remainder and mixed term. Start from exact Stieltjes summation with sum r_2(n)=pi x+P(x)-1 and accepted theta if helpful; do not replace a single summatory estimate by a sixfold approximation theorem. Try to obtain the target, not merely restate it. If the method self-returns or loses powers, give the strongest bound actually obtained and the exact quantitative first gap. Preserve all n>U and upper tails. One bounded analytical attempt and at most one targeted primary source check if essential. Seven sections and stop.',common),
('arithmetic_signed_tail_attack','discovery','selected_context',
 'Attack the full actual signed tail twelfth moment using r_2(n)=4 sum_(d|n)chi_4(d) or radial lattice Poisson/stationary phase. Choose a concrete complete arithmetic approach and push its estimates to their quantitative limit. Preserve chi_4 and all weights, frequency signs, dyadic recombination, errors, endpoints and infinite tail. A transform alone is not a result: show a saving or explicitly derive the net loss/self-return and the first new inequality needed. Do not subdivide indefinitely or discuss unrelated external methods. Seven sections and stop.',common),
('blind_filter_scale_audit','blind_rederiver','statement_only',
 'Independently solve the smoothing-scale and full-remainder statement in the isolated packet. No claimant or sibling reads. Seven sections and stop.',
 ['protocol.md',f'{base.as_posix()}/briefs/blind_filter_statement.md'])]
tasks=[]
for tid,role,access,target,ctx in specs:
 t=dict(id=tid,role=role,access_mode=access,status='pending',target=target,context_files=ctx,required_controls=controls,required_output=['Seven-section report with exact result, hypotheses, derivation, first gap, controls, dependencies, state effect.','Write only assigned report. No graph, draft, matrix, synthesis, source cards or successor work.'],report_path=f'{base.as_posix()}/reports/{tid}.md')
 if access=='statement_only':t['excluded_context']=['Graph, manifest, strategy, all prior/claimant/sibling derivations.']
 tasks.append(t)
m=dict(schema_version=1,round_index=203,round_type='complete_signed_analytic_attack',campaign_id=cid,title='Complete signed sixfold-convolution analytic attack',status='active',max_concurrency=3,coordinator='Codex',starting_graph_sha256=h,generated_at=now,
resource_policy=dict(analytical_algebraic_minimum_percent=100,numerical_experimental_maximum_percent=0,planned_numerical_percent=0,budget='Three bounded analytical reports, conductor independent radial analysis, and one repair/review cycle; no numerical experiments.'),
target_obligations=['GC-target','GC-external-Li-Yang-theta-star','GC-weighted-square-root-exact-resonance-mass','GC-physical-twelfth-moment-absolute-majorant-obstruction'],
frozen_target=dict(question='Can a complete coefficient-sensitive density or arithmetic estimate prove the actual signed filtered-convolution target with its full remainder?',reference_formula='||K_T*mu_(T,>floor(T^(1/2047)))^{*6}||_2 << T^(29/50+epsilon)',quantities=['Exact definitions in strategy/round203_complete_signed_convolution_attack.md.','Target gives only intermediate102/325; quarter theorem remains full goal.','All infinite tails, both cosine signs and sixfold/twelfth cross terms are retained.']),
completion_criteria=['Three bounded reports, with an independent statement-only filter/remainder control.','Each analytic attempt derives a bound and exact first missing inequality; no transform-only success.','Conductor independently reproduces material algebra and reconciles all power/error seams.','Reviewed exact kernel only if warranted; otherwise identity State Patch and unchanged proof draft.','Validate graph/patch, protected artifacts and round lifecycle before closure.'],controls=controls,
exit_labels=['complete_signed_norm_bound_proved','complete_analytic_attempt_no_new_bound'],tasks=tasks,
review_seams=[dict(id='remainder',requirement='Full arithmetic tails, both signs, all mixed terms and smoothing scales.'),dict(id='powers',requirement='Quantitative restored norm and moment exponents.'),dict(id='scope',requirement='Distinguish actual coefficient theorem from generic mechanism controls.')],scheduled_review='Next broad strategy/current-literature checkpoint205 after202--204.')
write('state/active_campaign.yml',m)
write('state/next_round_plan.yml',dict(round_index=203,status='active',campaign_id=cid,starting_graph_sha256=h,predecessor_round=202,design_choice=m['frozen_target']['question'],tasks=[t['id'] for t in tasks]))
p=Path('state/round_ledger.yml');s=p.read_text(encoding='utf-8');ledger=json.loads(s)
assert ledger['rounds'][-1]['round_index']==202 and ledger['rounds'][-1]['status']=='closed'
entry=dict(round_index=203,campaign_id=cid,type=m['round_type'],status='active',objective=m['frozen_target']['question'],tasks=[{k:t[k] for k in ['id','role','status']} for t in tasks],resource_policy=m['resource_policy'],starting_graph_sha256=h,exit_labels=m['exit_labels'],started_at=now)
head,tail=s.rsplit('\n  ]\n}',1)
new=(head+',\n'+'\n'.join('    '+line for line in json.dumps(entry,indent=2).splitlines())+'\n  ]\n}'+tail).replace('"active_round": 202','"active_round": 203',1)
ledger['active_round']=203;ledger['rounds'].append(entry);assert json.loads(new)==ledger
p.write_text(new,encoding='utf-8')
matrix=read('state/validation_matrix.yml');matrix.update(campaign_id=cid,promotion_status='round_203_active_no_promotion',graph_sha256=h,decision_rule='Round203 frozen complete signed analytic attack; no graph mutation or exponent improvement at launch.')
for t in tasks:matrix['gates'].append(dict(id='round203_'+t['id'],status='pending',artifact=t['report_path']))
matrix['gates'].append(dict(id='round203_conductor_reconciliation',status='pending',artifact=f'{base.as_posix()}/reviews/conductor_round203_reconciliation.md'))
write('state/validation_matrix.yml',matrix)
write(base/'controls/starting_state_hashes.json',{p:sha(p) for p in ['state/proof_obligations.yml','state/best_proof_draft.md','strategy/gauss_circle_strategy_review_2026-09-23.md']})
print('Round203 frozen; graph unchanged: '+h)
