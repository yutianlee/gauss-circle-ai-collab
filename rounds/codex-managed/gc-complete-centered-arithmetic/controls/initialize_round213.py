"""Freeze round213 once, only after verifying the closed212 archive."""
import hashlib,json,sys,time
from pathlib import Path
from datetime import datetime,timezone
root=Path.cwd();sys.path.insert(0,str(root))
from math_collab.campaigns import validate_campaign,prepare_campaign
from math_collab.proof_obligations import load_graph,validate_graph
cid='gc-complete-centered-arithmetic';base=Path('rounds/codex-managed')/cid
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def put(p,b):
 for i in range(5):
  try:Path(p).write_bytes(b);return
  except OSError:
   if i==4:raise
   time.sleep(.2)
def write(p,o):put(p,(json.dumps(o,indent=2,ensure_ascii=False)+'\n').encode())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
old=read('state/active_campaign.yml');assert old['round_index']==212 and old['status']=='complete'
prior=Path('rounds/codex-managed/gc-complete-four-point-correlation')
for p,h in read(prior/'controls/artifact_hashes.json').items():assert sha(p)==h,p
assert not (base/'plan.json').exists()
g=load_graph(Path('state/proof_obligations.yml'));assert len(g['proof_obligations'])==399 and not validate_graph(g,root=root)
h=sha('state/proof_obligations.yml');assert h==old['starting_graph_sha256']
strategy='strategy/round213_complete_centered_arithmetic_attack.md';now=datetime.now(timezone.utc).isoformat()
for d in ['briefs','reports','candidates','reviews','controls']:(base/d).mkdir(parents=True,exist_ok=True)
common=['protocol.md','state/proof_obligations.yml','state/active_campaign.yml',strategy,
prior.as_posix()+'/synthesis.md',prior.as_posix()+'/reports/four_point_local_arithmetic.md',
prior.as_posix()+'/reports/four_point_oscillatory_attack.md']
specs=[
('centered_divisor_attack','discovery','selected_context',
'Attack the complete actual model-subtracted four-point remainder using exact divisor, hyperbola or Gaussian norm arithmetic. Preserve all arms, characters, moduli, physical coefficients and model approximation/complement costs. Seek a complete quantitative saving, not an identity alone. Do not repeat outer-absolute CRT or the invalid fixed-shift Matthiesen import. At most one narrow primary theorem audit if useful. Use only the listed contexts and any precisely audited primary source; no siblings. Write seven sections and stop.',common),
('centered_shell_dispersion','discovery','selected_context',
'Attack the complete fixed-R signed product-shell energy of the actual remainder D-rho_loc I, preserving discrete-discrete, mixed and continuous model terms. Seek an upper bound sufficient after full shell weights, or an exact scoped obstruction with restored exponents. The modulus follows each complete n-sum; no radius-to-supremum transfer is free. At most one narrow primary theorem audit if useful. Do not simply repeat the uncentered positive Gram obstruction. No siblings. Write seven sections and stop.',common),
('blind_centered_certificate','blind_rederiver','statement_only',
'Derive or refute the precise positive centered-certificate test and sum-integral bridge in the isolated packet. Read only protocol and isolated packet; no web or other files. Write seven sections and stop.',
['protocol.md',base.as_posix()+'/briefs/blind_centered_certificate_statement.md'])]
controls=['actual_four_point_coefficients','complete_shifts_overlap','local_global_discrepancy','density_hypotheses','real_endpoints','all_restored_powers','signed_absolute_distinction','full_quarter_scope','statement_only_control']
tasks=[]
for ident,role,mode,target,ctx in specs:
 t=dict(id=ident,role=role,access_mode=mode,status='pending',target=target,context_files=ctx,required_controls=controls,
 required_output=['Seven numbered protocol sections with exact hypotheses, derivation, first unproved step, controls, dependencies and state recommendation.','Write only the assigned report; no shared state, synthesis, blind/sibling report or successor edits.'],report_path=base.as_posix()+'/reports/'+ident+'.md')
 if mode=='statement_only':t['excluded_context']=['Everything except protocol and isolated packet; exclude generated general brief, graph, strategy, all prior reports, siblings and web.']
 tasks.append(t)
m=dict(schema_version=1,round_index=213,round_type='complete_signed_model_remainder_attack',campaign_id=cid,title='Complete actual signed model remainder attack',status='active',max_concurrency=3,coordinator='Codex',starting_graph_sha256=h,generated_at=now,
resource_policy=dict(analytical_algebraic_minimum_percent=95,numerical_experimental_maximum_percent=5,planned_numerical_percent=0,budget='Three bounded reports; at most two narrow primary theorem audits, one per arithmetic task; one same-round seam cycle; planned zero experiments.'),
target_obligations=['GC-target','M9-M1','M9-M2','GC-complete-square-root-large-values-moment-bound'],
frozen_target=dict(question='Can the complete actual signed model remainder attain the selected power, or what exact scoped obstruction remains after centering and every cost?',reference_formula='sup_R (LK)^(-1)sum_Omega |D_(h,k)(R)-rho_loc_(h,k)I_(h,k)(R)| << T^(166/325+epsilon), uniformly throughout T^(166/325)<N<T^(242/325).',quantities=['Exact rounded L,K and actual four r2 factors; Omega contains all h!=k with Thk/N^(3/2)>1.','The bounded local candidate is not an established mean. Paid sectors and model integrals remain explicit. The102/325 milestone is not the quarter theorem.']),
completion_criteria=['Three bounded seven-section reports, including an isolated important derivation.','A complete quantitative bound or exact remaining arithmetic hypothesis with every sector and cost retained.','Independent mathematical/source seams and conductor synthesis at final hashes.','Validated State Patch and ledger closure before successor design; no unsupported exponent or parent promotion.'],
controls=controls,exit_labels=['complete_centered_gain_requires_validation','complete_signed_remainder_still_open','scoped_centered_certificate_obstruction'],tasks=tasks,
review_seams=[dict(id='complete_actual_arithmetic',requirement='Exact r2 coefficients, density/source uniformity, complete shifts and true modulus placement.'),dict(id='local_transfer_and_complete_power',requirement='All local endpoints, boundary terms, main terms, powers, full band and reconstruction.')],
previous_goal_turn_classification='progress_completed_validated212_actual_sector_controls_local_model_and_scoped_gram_obstruction',scheduled_review='Next mandatory broad strategy/current-primary-source review214 after211--213.')
assert not validate_campaign(m,g,root=root)
write('state/active_campaign.yml',m)
write('state/next_round_plan.yml',dict(round_index=213,status='active',campaign_id=cid,starting_graph_sha256=h,predecessor_round=212,tasks=[t['id'] for t in tasks]))
lp=Path('state/round_ledger.yml');raw=lp.read_bytes();s=raw.decode();ledger=json.loads(s)
assert ledger['rounds'][-1]['round_index']==212 and ledger['rounds'][-1]['status']=='closed'
entry=dict(round_index=213,campaign_id=cid,type=m['round_type'],status='active',objective=m['frozen_target']['question'],tasks=[{k:t[k] for k in ['id','role','status']} for t in tasks],resource_policy=m['resource_policy'],starting_graph_sha256=h,exit_labels=m['exit_labels'],started_at=now)
eol='\r\n' if '\r\n' in s else '\n';marker=eol+'  ]'+eol+'}';head,tail=s.rsplit(marker,1)
new=head+','+eol+eol.join('    '+line for line in json.dumps(entry,indent=2).splitlines())+marker+tail
new=new.replace('"active_round": 212','"active_round": 213',1);ledger['active_round']=213;ledger['rounds'].append(entry);assert json.loads(new)==ledger
put(lp,new.encode())
matrix=read('state/validation_matrix.yml');matrix.update(campaign_id=cid,promotion_status='round_213_active_no_promotion',graph_sha256=h,decision_rule='Complete signed model remainder attack; subtraction alone does not establish cancellation.')
for t in tasks:matrix['gates'].append(dict(id='round213_'+t['id'],status='pending',artifact=t['report_path']))
matrix['gates'].append(dict(id='round213_conductor_reconciliation',status='pending',artifact=base.as_posix()+'/reviews/conductor_round213_reconciliation.md'))
write('state/validation_matrix.yml',matrix)
write(base/'controls/starting_state_hashes.json',{p:sha(p) for p in ['state/proof_obligations.yml','state/best_proof_draft.md','strategy/gauss_circle_strategy_review_2026-09-23.md']})
failure=Path('state/failure_ledger.md');oldbytes=failure.read_bytes();prepare_campaign(m,g,root=root,graph_path=root/'state/proof_obligations.yml')
put(failure,oldbytes+b'\n\n## Round213 barriers\n\nThe complete actual model remainder is open. Centering by a bounded candidate is an identity, not a proved mean or cancellation estimate. The212 uncentered Gram obstruction must not be transferred to centered coefficients without proof. Every actual shift, support, model cross term and norm cost is retained. The invalid fixed-shift source import,210 CRT closure and211 scalar/bilinear failures are parked. Full quarter and all M1/M2 alternatives remain open; mandatory broad review214 follows this round.\n')
write(base/'controls/frozen_artifact_hashes.json',{p.as_posix():sha(p) for p in [base/'plan.json',Path(strategy)]+sorted((base/'briefs').glob('*.md'))})
for t in m['tasks']:t['status']='running'
write('state/active_campaign.yml',m);assert not validate_campaign(m,g,root=root)
print('Round213 frozen once; closed212 archive verified; three briefs ready; graph399 unchanged.')
