"""Close226 once after independent final-hash reviews. Never rerun after success."""
import copy,hashlib,json,re,subprocess,sys,time
from pathlib import Path
from datetime import datetime,timezone
root=Path.cwd();sys.path.insert(0,str(root))
from math_collab.campaigns import validate_campaign,_next_campaign
from math_collab.proof_obligations import load_graph,dump_graph,validate_graph,validate_patch_against_graph,apply_state_patch
cid='gc-full-goal-spectral-source-review';base=Path('rounds/codex-managed')/cid
gp=Path('state/proof_obligations.yml');draft=Path('state/best_proof_draft.md')
now=datetime.now(timezone.utc).isoformat()
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def put(p,b):
 for i in range(5):
  try:Path(p).write_bytes(b);return
  except OSError:
   if i==4:raise
   time.sleep(.2)
def write(p,o):put(p,(json.dumps(o,indent=2,ensure_ascii=False)+'\n').encode())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def contract(p):
 s=Path(p).read_text(encoding='utf-8')
 assert all(re.search(rf'^#{{1,2}} {i}\.',s,re.M) for i in range(1,8)),p
 return s
m=read('state/active_campaign.yml')
assert m['round_index']==226 and m['status']=='active' and m['campaign_id']==cid
assert not (base/'controls/artifact_hashes.json').exists(),'Already archived; never rerun'
start=read(base/'controls/starting_state_hashes.json')
assert all(sha(p)==h for p,h in start.items())
for p,h in read(base/'controls/frozen_artifact_hashes.json').items():assert sha(p)==h,('frozen',p)
entries=[e for e in read('state/round_ledger.yml')['rounds'] if 200<=e['round_index']<=225]
assert len(entries)==26 and all(e['status']=='closed' for e in entries)
count=0
for e in entries:
 for p,h in read(Path('rounds/codex-managed')/e['campaign_id']/'controls/artifact_hashes.json').items():
  assert sha(p)==h,('closed archive',p);count+=1
assert count==667
raw_graph=gp.read_bytes();raw_draft=draft.read_bytes();g=load_graph(gp)
assert len(g['proof_obligations'])==401 and not validate_graph(g,root=root)
assert not validate_campaign(m,g,root=root)
frozen=read(base/'plan.json')['campaign']
for key in ['frozen_target','completion_criteria','resource_policy','controls','target_obligations','review_seams']:assert m[key]==frozen[key]
assert len(m['tasks'])==len(frozen['tasks'])==3
for t,f in zip(m['tasks'],frozen['tasks']):
 assert {k:v for k,v in t.items() if k!='status'}=={k:v for k,v in f.items() if k!='status'}
 contract(t['report_path'])
for p,h in read(base/'controls/final_evidence_hashes.json').items():assert sha(p)==h,('final evidence',p)
attack=base/'reports/actual_shifted_spectral_sources.md'
profile=base/'reports/theta_wave_full_frontiers.md'
blind=base/'reports/blind_complex_subordination.md'
control=base/'controls/conductor_subordination_application.md'
packet=base/'briefs/blind_complex_subordination_statement.md'
assert 'not history-free' in contract(blind)
assert read(base/'controls/dispatch_provenance.json')['frozen_objective_changed'] is False
contract(control)
checkpoint=Path('strategy/gauss_circle_strategy_checkpoint_round226_2026-09-28.md')
status=base/'controls/conductor_current_primary_status.md'
reviews=[
 (base/'reviews/conductor_subordination_review.md',[blind,packet]),
 (base/'reviews/independent_shifted_source_review.md',[attack]),
 (base/'reviews/independent_theta_source_review.md',[profile]),
 (base/'reviews/independent_subordination_application_review.md',[control]),
 (base/'reviews/independent_strategy_checkpoint_review.md',[checkpoint,status]),
 (base/'reviews/conductor_complete_frontier_review.md',[attack,profile,blind,control,checkpoint])]
for p,arts in reviews:
 s=contract(p)
 assert 'GREEN' in s,p
 for a in arts:assert sha(a) in s.lower(),('review binding',p,a)
decision=read(base/'controls/closing_decision.json')
assert decision['graph_mutation'] is False and not decision['complete_frontier_bound_improved']
assert not decision['complete_moment_bound_improved'] and not decision['pointwise_exponent_change']
assert decision['terminal_label'] in m['exit_labels']
contract(base/'synthesis.md')
evidence=[Path(t['report_path']) for t in m['tasks']]+[control,packet,status,checkpoint]+[p for p,_ in reviews]+[base/'controls/dispatch_provenance.json',base/'controls/review_dispatch_provenance.json',base/'synthesis.md',base/'controls/closing_decision.json']
judge=base/'reviews/conductor_round226_reconciliation.md';s=contract(judge)
assert 'FINAL_HASH_BINDINGS' in s and 'GREEN for scoped spectral-source and subordination evidence only' in s
bindings='\n'.join(f'- {p.as_posix()}: {sha(p)}.' for p in evidence)
for p in base.rglob('*.md'):
 raw=p.read_bytes();content=raw.decode()
 assert not re.search(rb'\r(?!\n)',raw),p
 assert '\ufffd' not in content and not any(ord(c)<32 and c not in '\n\r\t' for c in content),p
protected=['GC-target','Conditional-bridge','M9','M9-M1','M9-M2','M9-endpoint-uniformity','M9-M1-global-angular-radial-estimate','M9-M1-global-lower-radial-signed-estimate','M9-M1-GAR-total-active-equivalence','GC-external-Li-Yang-theta-star','GC-complete-square-root-large-values-moment-bound','GC-complete-distinct-radical-twelfth-reduction']
patch=dict(round_index=226,campaign_id=cid,starting_graph_sha256=start[gp.as_posix()],
 proof_obligations=dict(create=[],update=[],correct_rejected=[],reject=[],no_change=protected),
 round_assessment=dict(terminal_label=decision['terminal_label'],reason=decision['reason']),
 reversibility=dict(rule='Identity in-memory application, inverse and replay; graph and proof-draft bytes never rewritten.'))
assert not validate_patch_against_graph(g,patch)
applied,result=apply_state_patch(copy.deepcopy(g),patch,round_index=226,judge_ref=judge.as_posix())
assert applied==g and not any([result.created,result.updated,result.rejected,result.corrected_rejected])
replay,_=apply_state_patch(copy.deepcopy(applied),patch,round_index=226,judge_ref=judge.as_posix())
assert replay==g and dump_graph(replay)==dump_graph(g)
assert not subprocess.check_output(['git','diff','--name-only','--','rounds/obligation-main','rounds/web-research-test']).strip()
subprocess.run(['git','diff','--check'],check=True)
# All mathematical review, hash, schema and replay checks precede shared-state writes.
put(judge,s.replace('FINAL_HASH_BINDINGS',bindings).encode())
write(base/'state_patch.json',patch)
preflight=dict(round_index=226,status='green_identity_patch_preflight',graph_schema='pass',campaign_schema='pass',
 identity_patch='pass',reverse_identity_replay='pass',all_401_nodes_unchanged=True,frozen_scope_and_briefs_unchanged=True,
 protected_archive_entries_checked=count,closed_round200_through225_archives_unchanged=True,
 mathematical_numerical_experiments=0,analytical_algebraic_percent_at_least=95,
 complete_moment_bound_improved=False,complete_frontier_bound_improved=False,pointwise_exponent_change=False)
write(base/'controls/closure_preflight.json',preflight)
matrix=read('state/validation_matrix.yml')
prior=copy.deepcopy([x for x in matrix['gates'] if not x['id'].startswith('round226_')])
assert len([x for x in matrix['gates'] if x['id'].startswith('round226_')])==4
for gate in matrix['gates']:
 if gate['id'].startswith('round226_'):gate['status']='green_scoped_evidence_full_targets_open'
for p,_ in reviews:matrix['gates'].append(dict(id='round226_'+p.stem,status='green',artifact=p.as_posix()))
matrix['gates'].append(dict(id='round226_identity_patch_scope',status='green',artifact=(base/'controls/closure_preflight.json').as_posix()))
gates=[x for x in matrix['gates'] if x['id'].startswith('round226_')]
assert len(gates)==11 and all(x['status'].startswith('green') and Path(x['artifact']).is_file() for x in gates)
assert prior==[x for x in matrix['gates'] if not x['id'].startswith('round226_')]
matrix.update(promotion_status='round_226_closed_identity_patch_spectral_review_no_complete_gain',graph_sha256=sha(gp),
 analytic_target_status='open_all_complete_full_proof_frontiers',decision_rule='Complete spectral source hypotheses, all parameters and subordination application reviewed. No complete analytic or exponent gain; upper certificates are not actual lower bounds.')
write('state/validation_matrix.yml',matrix)
assert gp.read_bytes()==raw_graph and draft.read_bytes()==raw_draft
assessment=dict(decision=decision['decision'],terminal_label=decision['terminal_label'],graph_mutation=False,
 main_result=decision['reason'],resulting_graph_sha256=sha(gp),patch_effect=f'0_create_0_update_0_correct_0_reject_{len(protected)}_no_change',
 complete_moment_bound_improved=False,complete_frontier_bound_improved=False,pointwise_exponent_change=False,
 goal_turn_classification=decision['goal_turn_classification'])
m.update(status='complete',completed_at=now,closing_assessment=assessment,
 post_report_reviews=[p.as_posix() for p,_ in reviews],conductor_interventions=decision['interventions'])
for t in m['tasks']:t['status']='completed'
assert not validate_campaign(m,g,root=root);write('state/active_campaign.yml',m)
lp=Path('state/round_ledger.yml');ledger_raw=lp.read_bytes();s=ledger_raw.decode();ledger=json.loads(s)
assert ledger['active_round']==226 and ledger['rounds'][-1]['round_index']==226
oldentries=copy.deepcopy(ledger['rounds'][:-1]);entry=ledger['rounds'][-1]
entry.update(status='closed',closing_assessment=assessment,completed_at=now,next_round=227)
for t in entry['tasks']:t['status']='completed'
matches=list(re.finditer(r'    \{\r?\n      "round_index": 226,',s));assert len(matches)==1
pos=matches[0].start();eol='\r\n' if '\r\n' in s else '\n'
new=s[:pos]+eol.join('    '+line for line in json.dumps(entry,indent=2,ensure_ascii=False).splitlines())+eol+'  ]'+eol+'}'+eol
assert json.loads(new)==ledger and ledger['rounds'][:-1]==oldentries
assert new[:pos].encode()==ledger_raw[:len(s[:pos].encode())];put(lp,new.encode())
write('state/next_round_plan.yml',dict(round_index=227,status='pending_design',campaign_id=None,tasks=[],starting_graph_sha256=sha(gp),
 predecessor_round=226,predecessor_terminal_label=decision['terminal_label'],candidate_objective=decision['next_objective'],
 candidate_method=decision['next_method'],first_unproved_estimate=decision['first_unproved_estimate'],
 exact_closed_dependencies=[p.as_posix() for p in evidence]+[judge.as_posix()],
 design_constraint='Design227 only after closed226 using its independently reviewed checkpoint. Attack one complete actual signed estimate with all costs; do not repeat absolute-Abel or heat-ray certificates. Preserve full quarter goal.',
 full_goal_scope='Quarter, sufficient unbounded fixed-order family and all complete M1/M2/GAR frontiers remain open.',
 scheduled_review='Next broad strategy/current-primary review229.',prior_turn_classification=assessment['goal_turn_classification']))
summary=_next_campaign(m,output_dir=base,graph_hash=sha(gp))+'\n## Closing decision\n\nRound226 mandatory source review closed with verified complete spectral costs and subordination controls. Identity State Patch; all401 nodes and proof-draft bytes unchanged. No complete estimate or exponent gain. Round227 analytic design pending; next mandatory review229.\n'
for p in ['state/current_round.md','state/next_campaign.md']:put(p,summary.encode())
note='\n## Round226 full-goal spectral-source review closure (2026-09-28)\n\n'+decision['state_note']+'\n'
for p in ['state/project_summary.md','state/current_state.md','state/failure_ledger.md']:
 raw=Path(p).read_bytes();assert b'## Round226 full-goal spectral-source review closure' not in raw;put(p,raw+note.encode())
assert all(sha(p)==h for p,h in start.items())
validation=dict(preflight,campaign_id=cid,generated_at=now,status='green_round226_closure_no_complete_gain',
 terminal_label=decision['terminal_label'],starting_graph_sha256=start[gp.as_posix()],final_graph_sha256=sha(gp),
 graph_nodes=401,original_graph_raw_bytes_unchanged=True,proof_draft_raw_bytes_unchanged=True,
 final_proof_draft_sha256=sha(draft),previous_ledger_prefix_bytes_unchanged=True,legacy_paths_unchanged=True,
 next_strategy_checkpoint=229,green_round_gates=len(gates))
write(base/'controls/closure_validation.json',validation)
vtext=f'''# Round226 closure validation

GREEN for scoped spectral-source and subordination evidence only. Full analytic
frontiers and the quarter goal remain OPEN. Identity patch validated,
applied in memory and replayed. All401 nodes, graph/draft bytes and
prior ledger prefix unchanged. All11 gates green; all667 prior archive
entries checked. Statement-only derivation and independent final-hash
application and primary-source checks complete. Zero mathematical experiments.
No complete estimate or pointwise exponent gain. Round227 pending design;
next broad strategy/current-primary review229.
Graph SHA256:{sha(gp)}.
Details:{base.as_posix()}/controls/closure_validation.json.
'''
for p in ['state/last_validation.md','state/last_validation_report.md']:put(p,vtext.encode())
assert not validate_graph(load_graph(gp),root=root) and not validate_campaign(read('state/active_campaign.yml'),g,root=root)
assert not subprocess.check_output(['git','diff','--name-only','--','rounds/obligation-main','rounds/web-research-test']).strip()
subprocess.run(['git','diff','--check'],check=True)
hashes={p.relative_to(root).as_posix():sha(p) for p in sorted((root/base).rglob('*')) if p.is_file() and p.name!='artifact_hashes.json' and '__pycache__' not in p.parts}
strategy=Path('strategy/round226_full_goal_spectral_source_review.md');hashes[strategy.as_posix()]=sha(strategy)
hashes[checkpoint.as_posix()]=sha(checkpoint)
write(base/'controls/artifact_hashes.json',hashes)
print(json.dumps({k:validation[k] for k in ['status','graph_nodes','final_graph_sha256','proof_draft_raw_bytes_unchanged','green_round_gates','protected_archive_entries_checked','pointwise_exponent_change']},indent=2))
