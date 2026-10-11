"""Freeze mandatory review220 once from the verified closed219 state."""
import hashlib,json,sys,time
from pathlib import Path
from datetime import datetime,timezone
root=Path.cwd();sys.path.insert(0,str(root))
from math_collab.campaigns import validate_campaign,prepare_campaign
from math_collab.proof_obligations import load_graph,validate_graph
cid='gc-full-goal-arithmetic-source-review';base=Path('rounds/codex-managed')/cid
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def put(p,b):
 for i in range(5):
  try:Path(p).write_bytes(b);return
  except OSError:
   if i==4:raise
   time.sleep(.2)
def write(p,o):put(p,(json.dumps(o,indent=2,ensure_ascii=False)+'\n').encode())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
old=read('state/active_campaign.yml');assert old['round_index']==219 and old['status']=='complete'
archive=read('rounds/codex-managed/gc-complete-anchored-divisor-energy/controls/artifact_hashes.json');assert len(archive)==28
for p,h in archive.items():assert sha(p)==h,p
assert not (base/'plan.json').exists()
g=load_graph(Path('state/proof_obligations.yml'));assert len(g['proof_obligations'])==401 and not validate_graph(g,root=root)
h=sha('state/proof_obligations.yml');assert h==old['closing_assessment']['resulting_graph_sha256']
strategy='strategy/round220_full_goal_arithmetic_source_review.md';now=datetime.now(timezone.utc).isoformat()
for d in ['briefs','reports','candidates','reviews','controls']:(base/d).mkdir(parents=True,exist_ok=True)
common=['protocol.md','state/proof_obligations.yml','state/active_campaign.yml',strategy,
'strategy/gauss_circle_strategy_review_2026-09-23.md','strategy/gauss_circle_strategy_checkpoint_round217_2026-09-28.md',
'proofs/kernels/gc_complete_square_root_large_values_moment_bound.md','proofs/kernels/gc_complete_distinct_radical_moment_reduction.md',
'rounds/codex-managed/gc-complete-anchored-divisor-energy/synthesis.md']
specs=[
('reciprocal_energy_sources','source_auditor','selected_context',
'Current primary-source search and at most TWO full theorem audits for the complete219 reciprocal-anchor real energy. Construct an exact source kernel and retain all integer aliases, real anchors, sigma/chi4, moving stars, coefficient norms and reconstruction costs. Choose a source-compatible theorem, not just a named family. Candidates: current all-moduli Kloosterman, reciprocal-fraction and large-sieve estimates. Rounding R_j² to an integer leaves an exact small smooth factor with K/A<=T^(-1/4); do not claim realness alone is fatal and do not discard that factor without a norm proof. A row=(j,a) bilinear theorem is not automatically a theorem requiring separate j/a factors. Produce a complete gain or first failed hypothesis and fully costed limitation. Bounded seven-section report only, exact primary links/versions/theorem numbers, no experiments, then stop.',common+[
'rounds/codex-managed/gc-complete-anchored-divisor-energy/reports/joint_cofactor_dispersion.md',
'rounds/codex-managed/gc-complete-anchored-divisor-energy/reviews/independent_dispersion_review.md',
'rounds/codex-managed/gc-full-source-method-review/reports/bilinear_arithmetic_sources.md']),
('full_frontier_sources','source_auditor','selected_context',
'Perform bounded current-primary-literature and full-goal strategy review across complete M1 HARD/SMOOTH, M2 TOP/BAL/UNBAL, total-M1 GAR and the unbounded-fixed-order moment family. Scope-screen new relevant harmonic/decoupling/spectral/arithmetic/geometric methods; fully audit at most TWO promising exact theorem statements with all costs and excluded ranges. Do not repeat old failed source names as progress. Identify a justified next full mathematical objective without starting it. Conductor separately checks Li-Yang and withdrawal records. Keep arbitrary sign controls separate from actual coefficients; fixed p does not prove quarter. Seven-section bounded report with exact links/versions/theorem numbers and a full-frontier comparison; no experiments or state edits, then stop.',common+[
'state/best_proof_draft.md','rounds/codex-managed/gc-full-goal-distinct-source-review/reports/full_frontier_sources.md',
'rounds/codex-managed/gc-full-source-method-review/reports/bilinear_arithmetic_sources.md']),
('blind_smooth_mask','blind_rederiver','statement_only',
'Solve only the isolated smooth-multiplier/row-interval operator statement, including exact product decomposition and unsupported-upgrade controls. Seven sections, no web/experiments, assigned report only, then stop.',
['protocol.md',base.as_posix()+'/briefs/blind_smooth_mask_statement.md'])]
controls=['current_primary_versions','exact_theorem_hypotheses','complete_kernel_map','coefficient_norms','all_aliases_and_endpoints','all_frontiers','full_exponent_restoration','actual_vs_enlarged_scope','statement_only_control','unbounded_fixed_order_scope']
tasks=[]
for ident,role,mode,target,ctx in specs:
 t=dict(id=ident,role=role,access_mode=mode,status='pending',target=target,context_files=ctx,required_controls=controls,required_output=['Seven numbered protocol sections; bounded exact source/application proof or no-go, first gap, controls, dependencies and state effect.','Only assigned report; no state, synthesis, sibling or successor work.'],report_path=base.as_posix()+'/reports/'+ident+'.md')
 if mode=='statement_only':t['excluded_context']=['All files except protocol and isolated packet; disclose prior-task history.']
 tasks.append(t)
m=dict(schema_version=1,round_index=220,round_type='mandatory_full_goal_strategy_source_review',campaign_id=cid,title='Full-goal arithmetic and current-source strategy review',status='active',max_concurrency=3,coordinator='Codex',starting_graph_sha256=h,generated_at=now,
resource_policy=dict(analytical_algebraic_minimum_percent=95,numerical_experimental_maximum_percent=5,planned_numerical_percent=0,budget='Three bounded reports, at most two full theorem audits per source role, one same-round review cycle and zero planned mathematical experiments.'),
target_obligations=['GC-target','M9-M1','M9-M2','GC-complete-square-root-large-values-moment-bound','GC-complete-distinct-radical-twelfth-reduction'],
frozen_target=dict(question='Does any current source, with a complete exact application and restored costs, advance a live full-proof frontier after217--219?',reference_formula='Full goal P(X)<<X^(1/4+epsilon); current anchored sufficient energy E<=J²v²TK/256+C_eta T^(208/2625+eta)JAK, with all other full frontiers retained.',quantities=['Actual real reciprocal-anchor energy with both modular signs and every integer alias, character, high-point sign and moving weight.','Exact smooth rounding factor retained with a proved norm cost; operator row=(j,a) versus product j/a hypotheses distinguished.','Every complete M1/M2/GAR frontier and sufficient unbounded-fixed-order family remains open.','A fixed twelfth milestone gives102/325 only; no component/source resemblance is a complete gain.']),
completion_criteria=['Two bounded current-primary-source/full-frontier reports and one isolated operator lemma report.','Exact hypothesis maps, full norms and restored powers, or precise failed imports; updated strategy checkpoint.','Independent final-hash source/mathematical/application seams, controls, validated patch and220 closure.'],controls=controls,
exit_labels=['complete_source_gain_requires_validation','strategy_source_review_no_complete_gain'],tasks=tasks,
review_seams=[dict(id='source_and_full_kernel',requirement='Primary theorem text, exact hypotheses, actual full kernel, exclusions and norm/restoration costs.'),dict(id='isolated_operator_application',requirement='Statement-only proof, controls and actual row/mask binding without unauthorized tensor upgrades.'),dict(id='full_goal_strategy',requirement='Full frontier comparison, unbounded-order requirement, qualified benchmarks and a justified next objective.')],
previous_goal_turn_classification='progress_completed_reviewed_evidence_changes_next_action_but_no_complete_estimate_gain',scheduled_review='This is mandatory220 review; next broad review223 after220--222.')
assert not validate_campaign(m,g,root=root)
write('state/active_campaign.yml',m);write('state/next_round_plan.yml',dict(round_index=220,status='active',campaign_id=cid,starting_graph_sha256=h,predecessor_round=219,tasks=[t['id'] for t in tasks]))
lp=Path('state/round_ledger.yml');s=lp.read_text(encoding='utf-8');ledger=json.loads(s)
assert ledger['rounds'][-1]['round_index']==219 and ledger['rounds'][-1]['status']=='closed'
entry=dict(round_index=220,campaign_id=cid,type=m['round_type'],status='active',objective=m['frozen_target']['question'],tasks=[{k:t[k] for k in ['id','role','status']} for t in tasks],resource_policy=m['resource_policy'],starting_graph_sha256=h,exit_labels=m['exit_labels'],started_at=now)
marker='\n  ]\n}';head,tail=s.rsplit(marker,1);new=head+',\n'+'\n'.join('    '+line for line in json.dumps(entry,indent=2).splitlines())+marker+tail
new=new.replace('"active_round": 219','"active_round": 220',1);ledger['active_round']=220;ledger['rounds'].append(entry);assert json.loads(new)==ledger;put(lp,new.encode())
matrix=read('state/validation_matrix.yml');matrix.update(campaign_id=cid,promotion_status='round_220_active_no_promotion',graph_sha256=h,decision_rule='Mandatory full-goal current-source review; no new theorem accepted at launch.')
for t in tasks:matrix['gates'].append(dict(id='round220_'+t['id'],status='pending',artifact=t['report_path']))
matrix['gates'].append(dict(id='round220_conductor_reconciliation',status='pending',artifact=base.as_posix()+'/reviews/conductor_round220_reconciliation.md'));write('state/validation_matrix.yml',matrix)
write(base/'controls/starting_state_hashes.json',{p:sha(p) for p in ['state/proof_obligations.yml','state/best_proof_draft.md','strategy/gauss_circle_strategy_review_2026-09-23.md']})
failure=Path('state/failure_ledger.md');oldbytes=failure.read_bytes();prepare_campaign(m,g,root=root,graph_path=root/'state/proof_obligations.yml')
put(failure,oldbytes+b'\n\n## Round220 full-goal source-review barriers\n\nRounds217--219 did not improve a complete moment. The219 inverse certificate is paid, but both signed modular kernels remain. Real anchors can be rounded only with an exact smooth-factor norm proof; combined-row operator hypotheses must not be enlarged from separate product factors. Current theorems need exact primary audits and full costs; source resemblance and smaller complements are not progress to a complete estimate.\n')
write(base/'controls/frozen_artifact_hashes.json',{p.as_posix():sha(p) for p in [base/'plan.json',Path(strategy)]+sorted((base/'briefs').glob('*.md'))})
for t in m['tasks']:t['status']='running'
write('state/active_campaign.yml',m);assert not validate_campaign(m,g,root=root)
print('Round220 frozen; closed219 archive28 verified; graph401 unchanged; three briefs ready.')
