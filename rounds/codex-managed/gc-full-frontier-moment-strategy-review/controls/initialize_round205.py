"""Freeze the scheduled full-frontier review after verified Round204 closure."""
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
root=Path.cwd(); sys.path.insert(0,str(root))
from math_collab.campaigns import validate_campaign
from math_collab.proof_obligations import load_graph, validate_graph
cid='gc-full-frontier-moment-strategy-review'
base=Path('rounds/codex-managed')/cid
for d in ['briefs','reports','candidates','reviews','controls']:
    (base/d).mkdir(parents=True,exist_ok=True)
def read(p): return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def write(p,o): Path(p).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
old=read('state/active_campaign.yml')
assert old['round_index']==204 and old['status']=='complete'
prior='rounds/codex-managed/gc-complete-large-values-duality'
for p,h in read(f'{prior}/controls/artifact_hashes.json').items(): assert sha(p)==h,p
h=sha('state/proof_obligations.yml')
assert h=='4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71'
g=load_graph(Path('state/proof_obligations.yml')); assert not validate_graph(g,root=root)
now=datetime.now(timezone.utc).isoformat()
strategy='strategy/round205_full_frontier_strategy_review.md'
common=['protocol.md','state/proof_obligations.yml','state/active_campaign.yml',strategy,
        f'{prior}/synthesis.md','strategy/gauss_circle_strategy_checkpoint_round202_2026-09-23.md']
controls=['complete_source_scope','actual_arithmetic_coefficients','current_primary_hypotheses',
          'withdrawals_and_versions','all_costs_restored','signed_absolute_distinction',
          'independent_gain_frontier','real_endpoint_uniformity','full_proof_scope','no_unproved_import']
specs=[
 ('current_circle_methods','source_auditor','selected_context',
  'Review current primary circle/moment/large-value and harmonic-analysis literature as of2026-09-26, including named withdrawals and any newly relevant method. Inspect theorem texts for at most three substantive candidates, prioritizing one beyond generic unweighted exponent pairs: arithmetic large values, amplitude-sensitive decoupling, restriction, or Dirichlet-polynomial large values. For each serious candidate state exact formula, coefficients, parameter/averaging domain, source location, and first transfer obstruction or a full costed implication for the actual series. Current metadata checks alone do not import a theorem. Compare to the complete Round204 high-value gap. Produce a ranked, quantified method recommendation with limits; no next-round launch.',
  common+['proofs/kernels/gc_complete_square_root_large_values_moment_bound.md',
          'rounds/codex-managed/gc-strategy-signed-moment-majorant-review/reports/current_primary_methods_audit.md',
          'sources/li_yang_2023.md']),
 ('internal_arithmetic_routes','source_auditor','selected_context',
  'Audit all complete internal M1/M2 frontiers and the complete original-t=1 source against a fresh modular/spectral alternative. Extract exact graph statements for M9/M1/M2 direct parents, GAR alternative and endpoint owners. Read the complete Round200 source and at most two additional exact evidence artifacts per shortlisted parent as needed, recording paths. Check current primary modular/trace-function theorem texts for at most two serious imports. Attempt an explicit arithmetic kernel identification or bounded transform on one complete source; retain real endpoints, physical coefficients, norms and exceptional moduli. Give full power ledger and first failed hypothesis if no transfer. Assess what a success actually closes and what remains. No unpriced name-list or next-round launch.',
  common+['strategy/gauss_circle_strategy_review_2026-09-23.md',
          'rounds/codex-managed/m9-m1-t1-complete-source-coefficient-mask-analysis/synthesis.md',
          'rounds/codex-managed/m9-m1-t1-complete-source-coefficient-mask-analysis/reports/complete_source_analytic_derivation.md',
          'rounds/codex-managed/gc-strategy-signed-moment-majorant-review/reports/current_primary_methods_audit.md']),
 ('blind_gain_frontier','blind_rederiver','statement_only',
  'Independently derive the exact gain frontier and no-self-bootstrap control from the isolated packet; no claimant/sibling context. Stop after report.',
  ['protocol.md',f'{base.as_posix()}/briefs/blind_gain_frontier_statement.md']),
]
tasks=[]
for ident,role,mode,target,context in specs:
    task=dict(id=ident,role=role,access_mode=mode,status='pending',target=target,context_files=context,
              required_controls=controls,required_output=['Seven numbered sections: result, hypotheses, derivation, first gap, controls, exact dependencies, state effect.','Write only assigned report; no state, draft, matrix, synthesis, source-card or successor edits.'],
              report_path=f'{base.as_posix()}/reports/{ident}.md')
    if mode=='statement_only':task['excluded_context']=['Graph, manifest, strategy, prior/claimant/sibling derivations and all sources.']
    tasks.append(task)
m=dict(schema_version=1,round_index=205,round_type='scheduled_full_frontier_strategy_review',
       campaign_id=cid,title='Full frontier and arithmetic gain strategy after the complete moment bound',
       status='active',max_concurrency=3,coordinator='Codex',starting_graph_sha256=h,generated_at=now,
       resource_policy=dict(analytical_algebraic_minimum_percent=100,numerical_experimental_maximum_percent=0,planned_numerical_percent=0,
       budget='Three bounded analytical/source reports, conductor independent synthesis, one parameter/source seam-review cycle if needed. No mathematical numerical experiments.'),
       target_obligations=['GC-target','M9','M9-M1','M9-M2','GC-complete-square-root-large-values-moment-bound'],
       frozen_target=dict(question='Which complete arithmetic objective and costed method should be attempted next toward the full quarter theorem?',
       reference_formula='P(X)<<X^(1/4+epsilon); current D(V)<<T^epsilon(V^-2+T V^(-136/13)); p12 milestone M12<<T^(29/25+epsilon).',
       quantities=['Assess complete original-t=1 Q_R target, all independent M1/M2 parents, and actual whole-discrepancy high values.',
                   'Current theta unchanged; beta=2theta-1/2; complete moment norm exponent5beta, target29/50.']),
       completion_criteria=['Three reports including isolated independent quantitative derivation.','Dated primary literature/version/withdrawal review with exact import costs and limitations.','Full frontier comparison and one concrete next objective with first unproved estimate.','Valid State Patch, ordinarily identity unless a separately reviewed new theorem is proved.','Keep the full goal and all existing source qualifications.'],
       controls=controls,exit_labels=['strategy_review_select_complete_arithmetic_objective','strategy_review_no_source_compatible_gain'],
       tasks=tasks,review_seams=[dict(id='gain_and_scope',requirement='Exact normalized powers, abstract controls and scope versus actual arithmetic.'),
       dict(id='source_application',requirement='Primary theorem hypotheses, actual coefficient/trace/mask costs and remaining parents.')],
       previous_goal_turn_classification='progress_validated_complete_distribution_moment_lemma_added',
       scheduled_review='This is the mandatory review after202--204; next broad review208 after205--207.')
# Validate paths before mutating state.
issues=validate_campaign(m,g,root=root); assert not issues,issues
write('state/active_campaign.yml',m)
write('state/next_round_plan.yml',dict(round_index=205,status='active',campaign_id=cid,starting_graph_sha256=h,
       predecessor_round=204,design_choice=m['frozen_target']['question'],tasks=[t['id'] for t in tasks]))
lp=Path('state/round_ledger.yml');s=lp.read_text(encoding='utf-8');ledger=json.loads(s)
assert ledger['rounds'][-1]['round_index']==204 and ledger['rounds'][-1]['status']=='closed'
entry=dict(round_index=205,campaign_id=cid,type=m['round_type'],status='active',objective=m['frozen_target']['question'],
           tasks=[{k:t[k] for k in ['id','role','status']} for t in tasks],resource_policy=m['resource_policy'],starting_graph_sha256=h,exit_labels=m['exit_labels'],started_at=now)
head,tail=s.rsplit('\n  ]\n}',1)
new=(head+',\n'+'\n'.join('    '+line for line in json.dumps(entry,indent=2).splitlines())+'\n  ]\n}'+tail).replace('"active_round": 204','"active_round": 205',1)
ledger['active_round']=205;ledger['rounds'].append(entry);assert json.loads(new)==ledger
lp.write_text(new,encoding='utf-8',newline='\n')
matrix=read('state/validation_matrix.yml');matrix.update(campaign_id=cid,promotion_status='round_205_active_no_promotion',graph_sha256=h,
       decision_rule='Mandatory strategy review; no new mathematical claim accepted at launch.')
for task in tasks:matrix['gates'].append(dict(id='round205_'+task['id'],status='pending',artifact=task['report_path']))
matrix['gates'].append(dict(id='round205_conductor_reconciliation',status='pending',artifact=f'{base.as_posix()}/reviews/conductor_round205_reconciliation.md'))
write('state/validation_matrix.yml',matrix)
write(base/'controls/starting_state_hashes.json',{p:sha(p) for p in ['state/proof_obligations.yml','state/best_proof_draft.md','strategy/gauss_circle_strategy_review_2026-09-23.md']})
print('Round205 frozen after verified204 closure; graph unchanged: '+h)
