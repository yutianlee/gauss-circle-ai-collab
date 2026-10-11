"""Freeze Round 201 workflow without changing the claim graph."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

cid='gc-whole-discrepancy-twelfth-moment'
base=f'rounds/codex-managed/{cid}'
old=json.loads(Path('state/active_campaign.yml').read_text(encoding='utf-8'))
assert old['round_index']==200 and old['status']=='complete'
h=hashlib.sha256(Path('state/proof_obligations.yml').read_bytes()).hexdigest()
assert h=='2f4448e999ab90387bca06498ddc60ee97b50f9900a9dfc6ad41fb201833c5f5'
now=datetime.now(timezone.utc).isoformat()
common=['protocol.md','state/proof_obligations.yml','state/active_campaign.yml',
        'strategy/round201_whole_discrepancy_twelfth_moment_strategy.md']
controls=['whole_discrepancy_scope','fixed_window_smoothing','inclusive_jump_error','bessel_and_fourier_normalization',
          'uniform_tail_control','all_sign_patterns','nonpairing_exact_resonances','displaced_offdiagonal_phase',
          'second_moment_normalization','moment_to_pointwise_exponents','primary_source_hypotheses','no_parent_or_exponent_overclaim']
specs=[
 ('whole_moment_analytic_attack','discovery','selected_context',
  'Derive the complete whole-discrepancy Poisson-Bessel expansion with delta=T^(-1/2) fixed across R~T, fixed a_n(T), exact all-sign twelfth-moment Fourier kernel, all errors/tails and real-radius endpoints. Reproduce the known second-moment upper exponent as normalization. Attack the complete twelfth-moment target, retaining signed displaced offdiagonal phase; if open, state its exact inequality and net eta deficit. You may audit primary standard Bessel/Poisson sources as needed and log exact hypotheses. Read only assigned context plus exact standard antecedents you identify. Write only your report.',
  common+['strategy/gauss_circle_strategy_review_2026-09-23.md','rounds/codex-managed/m9-m2-global-second-moment-exceptional-set/synthesis.md']),
 ('blind_exact_resonance_rederivation','blind_rederiver','statement_only',
  'Independently prove/refute the absolute weighted exact-resonance claim in the statement packet, including squarefree radical independence, all nonpairing configurations, uniformity and infinite limits. No finite-window near-resonance theorem may be inferred. Write only your seven-section report and stop.',
  ['protocol.md',f'{base}/briefs/blind_resonance_statement.md']),
 ('circle_moment_primary_source_audit','source_auditor','selected_context',
  'Search current primary literature for actual circle discrepancy moment estimates relevant to p=12. Audit normalization radius versus squared radius, signed versus absolute moments, allowed orders, weights, source versions/withdrawals, and constants/ranges. Inspect Zhai arXiv:0805.1523 and other genuinely relevant primary papers; a divisor theorem is not a circle theorem without an exact source transfer. Compute the complete p=12 bound implied by verified lower moments plus the accepted theta_LY and compare eta<13theta_LY-4. Do not silently extrapolate a fourth moment or import a new pointwise exponent. Record exact sources and the first failed hypothesis. Write only your report (including source cards within it); no shared source/graph edits.',
  common+['strategy/gauss_circle_strategy_review_2026-09-23.md','sources/li_yang_2023.md'])]
tasks=[]
for tid,role,access,target,ctx in specs:
 t=dict(id=tid,role=role,access_mode=access,status='pending',target=target,context_files=ctx,
        required_controls=controls,required_output=['Seven-section report with exact statements, proof/source audit, first open step, controls and state recommendation.','Write only assigned report; no shared-state edits or next round.'],report_path=f'{base}/reports/{tid}.md')
 if access=='statement_only':t['excluded_context']=['state/proof_obligations.yml','state/best_proof_draft.md','strategy review, active manifest, claimant or other historical derivations; only protocol and statement packet are permitted']
 tasks.append(t)
m=dict(schema_version=1,round_index=201,round_type='whole_discrepancy_twelfth_moment',campaign_id=cid,
 title='Whole-discrepancy twelfth moment: weighted source and exact resonances',status='active',max_concurrency=3,
 coordinator='Codex',starting_graph_sha256=h,generated_at=now,
 resource_policy=dict(analytical_algebraic_minimum_percent=100,numerical_experimental_maximum_percent=0,planned_numerical_percent=0,budget='Three bounded analytical/source reports and one repair/review cycle; no numerical experiments.'),
 target_obligations=['GC-target','GC-global-real-second-moment-density-one-quarter','GC-external-Li-Yang-theta-star'],
 frozen_target=dict(question='Can the complete whole-discrepancy twelfth moment be bounded by Y^(4+eta+epsilon) with eta<13theta_LY-4, using a fixed-window weighted square-root expansion; if not, what exact signed offdiagonal estimate and power gap remain?',
 reference_formula='T=sqrt(Y), delta=T^(-1/2), a_n(T)=r_2(n)n^(-3/4)Psi(sqrt(n/T)), H_T(R)=sum a_n(T)cos(2pi R sqrt(n)-3pi/4). Target int w(R/T)|H_T(R)|^12 dR << T^(1+2eta+epsilon). Expand all 2^12 signs with phase e(-3 sum signs/8) and T w-hat(-T sum signs sqrt(n)); retain nonzero differences signed.',
 quantities=['rho is fixed smooth radial nonnegative unit-mass compact disk support; w is fixed nonnegative smooth compactly supported away from zero and equals one on [1/sqrt(2),sqrt(3)].','The exact-resonance class includes nonpairing relations within one squarefree radical; no probabilistic independence on the finite radius interval is assumed.','Known low moments are normalization evidence, not a twelfth-moment theorem.','Moment-to-pointwise theta=(1+p/4+eta)/(p+1); at p=12 it is (4+eta)/13. This route does not discharge M1 or M2 obligations.']),
 completion_criteria=['Exact whole-source smoothing/Bessel/tail and twelfth-moment identities.','Independent all-configuration exact-resonance proof or counterexample.','Known second-moment normalization and audited current high-moment benchmark.','Complete target inequality or explicit signed offdiagonal estimate with quantitative remaining gap.','Independent seams, graph validation and a reversible State Patch before any promotion.'],
 controls=controls,exit_labels=['whole_discrepancy_twelfth_moment_improvement','whole_discrepancy_moment_reduction_open_offdiagonal'],tasks=tasks,
 review_seams=[dict(id=x,requirement=y) for x,y in [('source_normalization','Smoothing, Bessel constants, moving-radius errors, all signs and tails.'),('exact_resonance_algebra','Squarefree independence, full weighted resonant mass, no pairing-only shortcut.'),('moment_power_source_scope','Absolute moment source hypotheses, persistence bridge and restored exponent, no final theorem overclaim.')]],
 scheduled_review='Round 202 is the mandatory global strategy/current-primary-literature checkpoint after Rounds 199--201.')
Path('state/active_campaign.yml').write_text(json.dumps(m,indent=2)+'\n',encoding='utf-8')
Path('state/next_round_plan.yml').write_text(json.dumps(dict(round_index=201,status='active',campaign_id=cid,starting_graph_sha256=h,predecessor_round=200,design_choice='Campaign C: complete whole-discrepancy twelfth moment, independent of M1/M2.',tasks=[t['id'] for t in tasks]),indent=2)+'\n',encoding='utf-8')
p=Path('state/round_ledger.yml');s=p.read_text(encoding='utf-8');ledger=json.loads(s)
assert ledger['rounds'][-1]['round_index']==200 and ledger['rounds'][-1]['status']=='closed'
entry=dict(round_index=201,campaign_id=cid,type=m['round_type'],status='active',objective=m['frozen_target']['question'],tasks=[{k:t[k] for k in ['id','role','status']} for t in tasks],resource_policy=m['resource_policy'],starting_graph_sha256=h,exit_labels=m['exit_labels'],started_at=now)
head,tail=s.rsplit('\n  ]\n}',1)
new=(head+',\n'+'\n'.join('    '+line for line in json.dumps(entry,indent=2).splitlines())+'\n  ]\n}'+tail).replace('"active_round": 200','"active_round": 201',1)
ledger['active_round']=201;ledger['rounds'].append(entry);assert json.loads(new)==ledger
p.write_text(new,encoding='utf-8')
print('Round 201 frozen; graph unchanged:',h)
