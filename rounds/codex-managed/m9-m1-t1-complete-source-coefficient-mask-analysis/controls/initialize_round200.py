"""Conductor-only workflow initialization; does not mutate proof state."""
import hashlib
import json
from pathlib import Path
from datetime import datetime, timezone

root = Path.cwd()
cid = 'm9-m1-t1-complete-source-coefficient-mask-analysis'
base = f'rounds/codex-managed/{cid}'
graph_hash = hashlib.sha256(Path('state/proof_obligations.yml').read_bytes()).hexdigest()
assert hashlib.sha256(Path('state/proof_obligations.yml').read_bytes().replace(b'\r\n', b'\n')).hexdigest() == '3073235ad5677b9066f1336ec9d958b0e93b92d99cfa7ebea1d823146c799099'
old = json.loads(Path('state/active_campaign.yml').read_text(encoding='utf-8'))
assert old['round_index'] == 199 and old['status'] == 'complete'
now = datetime.now(timezone.utc).isoformat()
common = ['protocol.md', 'state/proof_obligations.yml', 'state/active_campaign.yml',
          'strategy/round200_complete_source_coefficient_mask_strategy.md']
source = [
 'proofs/kernels/m9_m1_hard_top_t1_comparable_factor_exchange_sector_and_residual_fejer_reduction.md',
 'proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md',
 'proofs/kernels/m9_m1_hard_top_small_t_primitive_ray_sector_and_truncated_mobius_self_return.md']
controls = ['complete_source_multiplicity', 'actual_coefficients_only', 'literal_endpoint_zero_extension',
 'partition_recombination', 'row_interval_vs_arithmetic_masks', 'product_and_projective_norms',
 'even_parity_connector', 'one_outer_real_part', 'net_power_ledger', 'no_capacity_lower_bound',
 'no_unverified_theorem_import', 'protected_parent_and_exponent_scope']
specs = [
 ('complete_source_analytic_derivation', 'discovery', 'selected_context',
  'Reconstruct the complete original-t=1 residual even-shift source before sector norms. Expand the actual normalized symbol by following only its exact antecedent definitions as needed. Give a common-domain coefficient/phase/support/multiplicity table and exact P_cl/P1/P2 recombination. Test natural arithmetic row/column coordinates and interval sections; seek the complete Re C_even << L^2 X^epsilon inequality, or identify the precise missing analytic estimate. Do not stop at the old P2 triangle no-go. Record every additional antecedent read. Write only your assigned report.',
  common + source + ['strategy/gauss_circle_strategy_review_2026-09-23.md', 'proofs/kernels/m9_m1_hard_top_t1_p2_cross_gcd_cellular_boundary_self_return.md']),
 ('actual_symbol_norm_power_audit', 'seam_reviewer', 'selected_context',
  'Independently audit the full actual source coefficients, all masks and a quantitative product/projective-norm interface. Determine which geometric row sections are intervals, which arithmetic masks remain inside the kernel/amplitude, and whether an affordable norm is actually proved. Give raw L^3 correlation capacity versus L^2 target, high-h Y loss only as a subsidiary ledger, and scalar reconstruction. Display an explicit all-cost conditional inequality for a source-compatible bilinear import; do not claim a Kloosterman kernel or imported saving without proof. Follow exact symbol antecedents as needed and log them. Write only your assigned report.',
  common + source + ['strategy/gauss_circle_strategy_review_2026-09-23.md']),
 ('blind_interval_operator_rederivation', 'blind_rederiver', 'statement_only',
  'Independently prove or refute every finite statement in the independent statement packet, including interval-mask, mixed-amplitude norm, commutator and even-parity connector statements. Do not infer any arithmetic saving. Produce a seven-section report and stop.',
  ['protocol.md', f'{base}/briefs/independent_statement_packet.md'])]
tasks=[]
for tid,role,access,target,ctx in specs:
 t=dict(id=tid,role=role,access_mode=access,status='pending',target=target,context_files=ctx,
        required_controls=controls,required_output=['Seven-section protocol report with exact hypotheses, proof, first open step, controls, dependencies and state recommendation.','No shared-state edits; stop after the assigned report.'],report_path=f'{base}/reports/{tid}.md')
 if access=='statement_only':
  t['excluded_context']=['state/proof_obligations.yml','state/best_proof_draft.md','strategy review and all claimant or historical derivations; read only protocol and the independent statement packet']
 tasks.append(t)
manifest=dict(schema_version=1,round_index=200,round_type='complete_source_coefficient_mask_analysis',
 campaign_id=cid,title='Complete original-t=1 source: coefficients, masks and net power',status='active',
 max_concurrency=3,coordinator='Codex',starting_graph_sha256=graph_hash,generated_at=now,
 resource_policy=dict(analytical_algebraic_minimum_percent=100,numerical_experimental_maximum_percent=0,planned_numerical_percent=0,budget='Three analytical reports, one bounded correction/review cycle, conductor synthesis. No numerical experiments.'),
 target_obligations=['M9-M1-hard-top-high-radical-small-t-residual-estimate','M9-M1-hard-top-t1-comparable-factor-exchange-sector','M9-M1-hard-top-t1-residual-fejer-tangent-gcd-reduction'],
 frozen_target=dict(question='Can the complete original-t=1 residual even-shift source, with P1 and P2 recombined, be bounded at L^2 X^epsilon; otherwise what exact coefficient norm or unmasked analytic estimate is missing after every mask and reconstruction cost?',
 reference_formula='C_even=sum_(0<r<R0, 2|r)(1-r/R0) sum_N c_(N+r,sigma)^rem conjugate(c_(N,sigma)^rem) e(sigma sqrt(X) r/(sqrt(N+r)+sqrt(N))), R0=ceil(L). Target Re C_even << L^2 X^epsilon; c and total zero-extended lambda are exactly K185.1--3. E_R<=2D+4Re C_even and scalar prefactor O(L).',
 quantities=['Complete source precedes P_cl/P1/P2, both opposing orientations, all gcd/height/packet splits and later T branches.','A partition identity removes artificial partition boundaries only for a common genuine transport; it provides no analytic saving.','Geometric interval masks require a proved unmasked all-vector bilinear estimate and a controlled product or projective norm.','No t>=2, complete M1/M2, bridge, target or exponent conclusion is implied by a t=1 result.']),
 completion_criteria=['Complete physical source and literal amplitude/support/multiplicity table.','Independent finite interval, projective-norm and parity connector derivations.','Quantified actual-symbol mask/norm and restored power ledger.','Complete target proof or explicit conditional interface locating the first unresolved analytic estimate; no endless smaller complements.','Conductor seam reconciliation and mechanical campaign/graph validation before closure; proof promotion requires all separate State Patch gates.'],
 controls=controls,exit_labels=['complete_t1_residual_target_proved','complete_source_interface_with_open_estimate'],tasks=tasks,
 review_seams=[dict(id=x,requirement=y) for x,y in [
 ('source_and_multiplicity','Check common physical source, actual symbol, arithmetic deletions, all endpoints and multiplicity.'),
 ('interval_and_norm','Check independent row-interval proof, correct complex projective norm and actual applicability.'),
 ('power_and_scope','Check even-parity connector, full versus high-h capacity, every reconstruction cost and protected scope.')]],
 scheduled_review='Round 202 remains the full-proof strategy/current-primary-literature checkpoint; no successor is launched in Round 200.')
Path('state/active_campaign.yml').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
Path('state/next_round_plan.yml').write_text(json.dumps(dict(round_index=200,status='active',campaign_id=cid,starting_graph_sha256=graph_hash,predecessor_round=199,design_choice='Campaign A: recombine complete original-t=1 residual source; user-requested strategy review supersedes historical P1-or-P2-only workflow.',strategy_file='strategy/round200_complete_source_coefficient_mask_strategy.md',tasks=[t['id'] for t in tasks],proof_state_effect='none_at_launch'),indent=2)+'\n',encoding='utf-8')
ledger_text=Path('state/round_ledger.yml').read_text(encoding='utf-8')
ledger=json.loads(ledger_text)
key=next(k for k,v in ledger.items() if isinstance(v,list) and v and isinstance(v[-1],dict) and 'round_index' in v[-1])
assert ledger[key][-1]['round_index']==199 and ledger[key][-1]['status']=='closed'
ledger['active_round']=200
ledger[key].append(dict(round_index=200,campaign_id=cid,type=manifest['round_type'],status='active',objective=manifest['frozen_target']['question'],tasks=[{k:t[k] for k in ['id','role','status']} for t in tasks],resource_policy=manifest['resource_policy'],starting_graph_sha256=graph_hash,exit_labels=manifest['exit_labels'],started_at=now))
head,tail=ledger_text.rsplit('\n  ]\n}',1)
entry_text='\n'.join('    '+line for line in json.dumps(ledger[key][-1],indent=2,ensure_ascii=False).splitlines())
new_ledger=(head+',\n'+entry_text+'\n  ]\n}'+tail).replace('"active_round": 199','"active_round": 200',1)
assert json.loads(new_ledger)==ledger
Path('state/round_ledger.yml').write_text(new_ledger,encoding='utf-8')
print('Round 200 workflow frozen; graph untouched:',graph_hash)
