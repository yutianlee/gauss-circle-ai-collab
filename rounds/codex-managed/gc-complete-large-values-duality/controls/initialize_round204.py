"""Freeze the complete large-values round after validated203 closure."""
import json,hashlib
from pathlib import Path
from datetime import datetime,timezone
cid='gc-complete-large-values-duality';base=Path('rounds/codex-managed')/cid
for d in ['briefs','reports','candidates','reviews','controls']:(base/d).mkdir(parents=True,exist_ok=True)
def read(p):return json.loads(Path(p).read_text(encoding='utf-8'))
def write(p,o):Path(p).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
old=read('state/active_campaign.yml');assert old['round_index']==203 and old['status']=='complete'
h=sha('state/proof_obligations.yml');assert h=='abc88f6cd29d757b880037b6f600b802a22ac4b57fcce40662205150f3ed8ceb'
for p,v in read('rounds/codex-managed/gc-complete-signed-convolution-attack/controls/artifact_hashes.json').items():assert sha(p)==v
now=datetime.now(timezone.utc).isoformat();strategy='strategy/round204_complete_large_values_attack.md'
prior='rounds/codex-managed/gc-complete-signed-convolution-attack'
common=['protocol.md','state/proof_obligations.yml','state/active_campaign.yml',strategy,f'{prior}/synthesis.md']
controls=['actual_coefficients','complete_distribution','full_diagonal_and_ceiling','source_hypotheses','all_tails_and_ranges','real_uniformity','net_moment_and_pointwise_powers','independent_statement_only_control','no_parent_overclaim']
specs=[
('actual_large_values_attack','discovery','selected_context',
 'Attack the frozen full actual large-value distribution using finite-vector duality and localized Gram matrices. Prove or refute the candidate D(V)<<T^epsilon(V^-2+T V^(-136/13)) by deriving the correlation interpolation from the accepted source card plus elementary derivatives, all small-u regimes, real level-set covering and full dyadic/tail recombination. Preserve all diagonal and ceiling terms. Then attempt the coefficient-sensitive improvement needed to reach the frozen target; identify exactly why any generic bound falls short. Derive the best complete moment consequence with the accepted pointwise exponent only after pricing its exact smoothing interface; do not just substitute into a printed endpoint. Seven sections and stop.',
 common+['sources/bourgain_2017_exponent_pair.md',f'{prior}/reports/arithmetic_signed_tail_attack.md','rounds/codex-managed/gc-strategy-signed-moment-majorant-review/reports/signed_cutoff_tail_moment_audit.md']),
('large_values_primary_source_audit','source_auditor','selected_context',
 'Audit primary sources for this specific complete large-values attempt. Check Bourgain2017 global Theorem6 on f(n)=u sqrt(n), its derivative class, proper intervals and all source parameter ranges; compare interpolation with the elementary second derivative estimate and the proposed exponent13/55. Independently audit the original circle large-values/moment trail (Ivic1990, published Tsang-Zhai q0 benchmark, or directly accessible primary proof) for whether q0=262/27 is fixed by an older pointwise exponent and exactly what an update would require. Prioritize at most two full primary proofs. Do not guess a new endpoint. Report applicability, exact theorem locations and costs, including negative conclusions. Seven sections, write only report and stop.',
 common+['sources/bourgain_2017_exponent_pair.md','rounds/codex-managed/gc-whole-discrepancy-twelfth-moment/reports/circle_moment_primary_source_audit.md','rounds/codex-managed/gc-strategy-signed-moment-majorant-review/reports/signed_cutoff_tail_moment_audit.md']),
('blind_gram_covering_audit','blind_rederiver','statement_only',
 'Solve the isolated Gram/covering problem independently, retaining diagonal, localization ceilings and a one-peak aligned control. No claimant or sibling reads. Seven sections and stop.',
 ['protocol.md',f'{base.as_posix()}/briefs/blind_gram_statement.md'])]
tasks=[]
for tid,role,access,target,ctx in specs:
 t=dict(id=tid,role=role,access_mode=access,status='pending',target=target,context_files=ctx,required_controls=controls,required_output=['Seven-section report: result, exact hypotheses, proof, first gap, controls, dependencies, state effect.','Write only assigned report; no graph/draft/matrix/synthesis/source-card/successor edits.'],report_path=f'{base.as_posix()}/reports/{tid}.md')
 if access=='statement_only':t['excluded_context']=['Graph, manifest, strategy, source cards, every prior/claimant/sibling derivation.']
 tasks.append(t)
m=dict(schema_version=1,round_index=204,round_type='complete_large_values_analytic_attack',campaign_id=cid,title='Actual square-root large values with full Gram diagonal',status='active',max_concurrency=3,coordinator='Codex',starting_graph_sha256=h,generated_at=now,
 resource_policy=dict(analytical_algebraic_minimum_percent=100,numerical_experimental_maximum_percent=0,planned_numerical_percent=0,budget='Three bounded analytical/source reports, conductor independent derivation, and one repair/seam-review cycle. No mathematical numerical experiments.'),
 target_obligations=['GC-target','GC-external-Li-Yang-theta-star','Bourgain-2017-reciprocal-exponent-pair-source-audit','GC-physical-twelfth-moment-absolute-majorant-obstruction'],
 frozen_target=dict(question='Can actual finite-vector large-values analysis prove the complete high-value distribution required by the twelfth-moment target?',reference_formula='D_T(V)<<T^(29/25+epsilon)V^(-12) for T^(54/775)<=V<=T^(beta+epsilon), beta=2theta_LY-1/2',quantities=['Exact actual B_T and window in frozen strategy.','Candidate weaker envelope T^epsilon(V^-2+T V^(-136/13)) must be proved, not assumed.','Keep the complete diagonal, all localization intervals and upper tails; a generic aligned counterexample is not an arithmetic counterexample.']),
 completion_criteria=['Three bounded reports and a statement-only independent Gram/covering control.','Complete actual level-set inequality or exact first failed step with no lost diagonal, ceiling or tail.','Primary square-root source applicability and all powers independently checked.','Any new complete proved kernel receives exact-hash independent reviews and graph validation; otherwise identity patch.','Distinguish better moments from pointwise progress and keep full quarter goal.'],controls=controls,
 exit_labels=['complete_target_distribution_proved','complete_distribution_gain_target_open','large_values_attempt_no_new_bound'],tasks=tasks,
 review_seams=[dict(id='duality_covering',requirement='Finite Gram normalization, sample separation, all localization regimes.'),dict(id='source_and_moments',requirement='Exact source class and complete error/exponent reconstruction.'),dict(id='scope',requirement='Actual weights versus generic controls; moment versus pointwise improvement.')],
 previous_goal_turn_classification='progress_completed_analytic_attempt_changed_next_action_no_exponent_gain',scheduled_review='Round205 mandatory broad strategy/current-literature review after202--204.')
write('state/active_campaign.yml',m)
write('state/next_round_plan.yml',dict(round_index=204,status='active',campaign_id=cid,starting_graph_sha256=h,predecessor_round=203,design_choice=m['frozen_target']['question'],tasks=[t['id'] for t in tasks]))
p=Path('state/round_ledger.yml');s=p.read_text(encoding='utf-8');ledger=json.loads(s)
assert ledger['rounds'][-1]['round_index']==203 and ledger['rounds'][-1]['status']=='closed'
entry=dict(round_index=204,campaign_id=cid,type=m['round_type'],status='active',objective=m['frozen_target']['question'],tasks=[{k:t[k] for k in ['id','role','status']} for t in tasks],resource_policy=m['resource_policy'],starting_graph_sha256=h,exit_labels=m['exit_labels'],started_at=now)
head,tail=s.rsplit('\n  ]\n}',1);new=(head+',\n'+'\n'.join('    '+line for line in json.dumps(entry,indent=2).splitlines())+'\n  ]\n}'+tail).replace('"active_round": 203','"active_round": 204',1)
ledger['active_round']=204;ledger['rounds'].append(entry);assert json.loads(new)==ledger;p.write_text(new,encoding='utf-8')
matrix=read('state/validation_matrix.yml');matrix.update(campaign_id=cid,promotion_status='round_204_active_no_promotion',graph_sha256=h,decision_rule='Round204 frozen actual large-values attack; no new bound accepted at launch.')
for t in tasks:matrix['gates'].append(dict(id='round204_'+t['id'],status='pending',artifact=t['report_path']))
matrix['gates'].append(dict(id='round204_conductor_reconciliation',status='pending',artifact=f'{base.as_posix()}/reviews/conductor_round204_reconciliation.md'))
write('state/validation_matrix.yml',matrix)
write(base/'controls/starting_state_hashes.json',{p:sha(p) for p in ['state/proof_obligations.yml','state/best_proof_draft.md','strategy/gauss_circle_strategy_review_2026-09-23.md']})
print('Round204 frozen; graph unchanged: '+h)
