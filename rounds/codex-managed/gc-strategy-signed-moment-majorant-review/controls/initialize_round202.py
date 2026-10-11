"""Freeze the scheduled strategy review and its three bounded interfaces."""
import json, hashlib
from pathlib import Path
from datetime import datetime, timezone

cid='gc-strategy-signed-moment-majorant-review'
base=Path('rounds/codex-managed')/cid
old=json.loads(Path('state/active_campaign.yml').read_text(encoding='utf-8'))
assert old['round_index']==201 and old['status']=='complete'
h=hashlib.sha256(Path('state/proof_obligations.yml').read_bytes()).hexdigest()
assert h=='682cb189a3ab0ef26f8d19701e2949547446d37505df01f7b7eaf1cfdd0f359c'
now=datetime.now(timezone.utc).isoformat()
strategy='strategy/round202_strategy_literature_signed_moment_review.md'
common=['protocol.md','state/proof_obligations.yml','state/active_campaign.yml',strategy]
r200='rounds/codex-managed/m9-m1-t1-complete-source-coefficient-mask-analysis/synthesis.md'
r201='rounds/codex-managed/gc-whole-discrepancy-twelfth-moment'
controls=['complete_source_scope','physical_coefficients','current_primary_hypotheses','withdrawals_and_versions','signed_absolute_distinction','all_costs_restored','exact_nonzero_resonance_split','real_endpoint_uniformity','independent_statement_only_control','full_proof_frontier','no_parent_or_exponent_overclaim']
specs=[
('current_primary_methods_audit','source_auditor','selected_context',
 'Perform the scheduled dated current-primary-literature review for the full Gauss circle goal. Use the actual Round-200 and Round-201 complete interfaces. Check strongest claims and withdrawals, then audit a bounded set of recent decoupling/amplitude, bilinear Kloosterman, trace-function or spectral methods from the supplied strategy. Match exact arithmetic kernel, coefficient class, modulus, lengths, averaging variable, norm costs and endpoints. Prioritize full theorem text and at most two concrete potential imports. Do not repeat prior audits without checking what changed; report first unmet hypothesis and net exponent, not paper names. Current leads include Blomer-Pascadi 2607.24311, Pascadi 2511.08445, Milicevic-Qin-Wu 2511.07550, Fouvry-Kowalski-Michel-Sawin 2511.09459, and amplitude-dependent cone methods. Bounded corpus, no universal literature claim. Seven-section report; no sibling reads or shared edits.',
 common+['strategy/gauss_circle_strategy_review_2026-09-23.md',r200,f'{r201}/synthesis.md',f'{r201}/reports/circle_moment_primary_source_audit.md','sources/li_yang_2023.md']),
('signed_cutoff_tail_moment_audit','discovery','selected_context',
 'Derive and audit a complete cutoff-dependent route to the actual twelfth moment. Split H_T into n<=U and n>U, keep actual coefficients and fixed window. Inspect primary circle higher-moment/large-values methods for their actual residual or truncated-series estimates and ranges (Zhai II 0805.1270 and applicable original sources). Determine whether those estimates, with exact full tails and accepted theta_LY, beat eta_0=(62/27)(theta_LY-1/4); do not guess a new admissible q by substituting theta. Give a concrete sufficient signed tail inequality with complete T,U exponent accounting, and identify the first new estimate needed. Address why known low moments do not imply a twelfth moment. Work independently of sibling reports; no shared edits. Seven-section report and stop.',
 common+[f'{r201}/synthesis.md',f'{r201}/reports/whole_moment_analytic_attack.md',f'{r201}/reports/circle_moment_primary_source_audit.md']),
('blind_physical_near_resonance_mass','blind_rederiver','statement_only',
 'Prove or refute the actual-coefficient positive near-resonance statement from the isolated packet, including nonzero-frequency deletion and exact consequence for termwise absolute majorants. Preserve statement-only isolation. Seven-section report and stop.',
 ['protocol.md',(base/'briefs/blind_physical_mass_statement.md').as_posix()])]
tasks=[]
for tid,role,access,target,ctx in specs:
 t=dict(id=tid,role=role,access_mode=access,status='pending',target=target,context_files=ctx,required_controls=controls,required_output=['Seven-section report: result, hypotheses, proof, first open step, controls, dependencies, state recommendation.','Write only assigned report; no graph, draft, synthesis, validation, source-card or next-round edits.'],report_path=(base/'reports'/f'{tid}.md').as_posix())
 if access=='statement_only':t['excluded_context']=['Graph, proof draft, manifest, strategy, all claimant/sibling or historical derivations.']
 tasks.append(t)
m=dict(schema_version=1,round_index=202,round_type='scheduled_strategy_literature_and_signed_moment_gate',campaign_id=cid,title='Scheduled strategy review and physical signed-moment majorant gate',status='active',max_concurrency=3,coordinator='Codex',starting_graph_sha256=h,generated_at=now,
resource_policy=dict(analytical_algebraic_minimum_percent=100,numerical_experimental_maximum_percent=0,planned_numerical_percent=0,budget='Three bounded analytical/source reports and one repair/seam-review cycle. No numerical experiments.'),
target_obligations=['GC-target','GC-external-Li-Yang-theta-star','GC-weighted-square-root-exact-resonance-mass','M9-M1','M9-M2'],
frozen_target=dict(question='Which complete signed analytic route survives the current-source and actual-coefficient majorant audit and merits the next campaign toward the quarter theorem?',reference_formula='Round200 actual Q_R<<L^2 X^epsilon; Round201 actual O_12(T)<<T^(1+2eta+epsilon), eta<13theta_LY-4. Test physical nonzero balanced near-resonance positive subsum >=c T^(5/2) and audit cutoff-tail alternatives; do not infer a signed-moment lower bound.',quantities=['T=sqrt(Y), fixed a_n(T)=r_2(n)n^(-3/4)Psi(sqrt(n/T)); w fixed supported away from zero.','Existing graph/exponents remain authoritative. Any majorant no-go concerns only termwise absolute Fourier expansion.','Any successor must preserve the actual source and restore all coefficient, cutoff, tail and reconstruction powers.']),
completion_criteria=['Dated primary-source and full-frontier review.','Independent physical majorant proof/refutation with exact resonance deletion.','Complete cutoff-dependent signed-tail sufficient inequality and source gap.','One conductor strategy choice justified by reviewed evidence.','Required seams and mechanically reversible State Patch; no exponent overclaim.'],controls=controls,
exit_labels=['strategy_review_with_complete_signed_next_target','strategy_review_no_source_compatible_gain'],tasks=tasks,
review_seams=[dict(id='physical_majorant',requirement='Independent physical coefficients, real endpoints, nonzero exclusion, signed-scope control.'),dict(id='source_and_tail',requirement='Primary theorem conditions and complete cutoff exponent bookkeeping.'),dict(id='full_proof_strategy',requirement='Compare complete routes and select one exact next inequality without treating mechanism exclusions as exponent gain.')],scheduled_review='Round202 satisfies review after199--201. Next checkpoint Round205 after202--204.')
def write(p,obj):Path(p).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
write('state/active_campaign.yml',m)
write('state/next_round_plan.yml',dict(round_index=202,status='active',campaign_id=cid,starting_graph_sha256=h,predecessor_round=201,design_choice=m['frozen_target']['question'],tasks=[t['id'] for t in tasks]))
p=Path('state/round_ledger.yml');s=p.read_text(encoding='utf-8');ledger=json.loads(s)
assert ledger['rounds'][-1]['round_index']==201 and ledger['rounds'][-1]['status']=='closed'
entry=dict(round_index=202,campaign_id=cid,type=m['round_type'],status='active',objective=m['frozen_target']['question'],tasks=[{k:t[k] for k in ['id','role','status']} for t in tasks],resource_policy=m['resource_policy'],starting_graph_sha256=h,exit_labels=m['exit_labels'],started_at=now)
head,tail=s.rsplit('\n  ]\n}',1)
new=(head+',\n'+'\n'.join('    '+line for line in json.dumps(entry,indent=2).splitlines())+'\n  ]\n}'+tail).replace('"active_round": 201','"active_round": 202',1)
ledger['active_round']=202;ledger['rounds'].append(entry);assert json.loads(new)==ledger
p.write_text(new,encoding='utf-8')
matrix=json.loads(Path('state/validation_matrix.yml').read_text(encoding='utf-8'))
matrix.update(campaign_id=cid,promotion_status='round_202_active_no_promotion',graph_sha256=h)
for tid,_,_,_,_ in specs:matrix['gates'].append(dict(id='round202_'+tid,status='pending',artifact=(base/'reports'/f'{tid}.md').as_posix()))
matrix['gates'].append(dict(id='round202_conductor_reconciliation',status='pending',artifact=(base/'reviews/conductor_round202_reconciliation.md').as_posix()))
write('state/validation_matrix.yml',matrix)
write(base/'controls/starting_state_hashes.json',{p:hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in ['state/proof_obligations.yml','state/best_proof_draft.md','strategy/gauss_circle_strategy_review_2026-09-23.md']})
print('Round202 frozen, graph unchanged:',h)
