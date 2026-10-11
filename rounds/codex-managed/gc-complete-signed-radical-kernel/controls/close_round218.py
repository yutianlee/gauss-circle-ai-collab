"""Close the complete joint-kernel attempt with a validated identity patch."""
import copy, hashlib, json, re, subprocess, sys, time
from datetime import datetime, timezone
from pathlib import Path
root=Path.cwd();sys.path.insert(0,str(root))
from math_collab.campaigns import validate_campaign,_next_campaign
from math_collab.proof_obligations import load_graph,dump_graph,validate_graph,validate_patch_against_graph,apply_state_patch
cid='gc-complete-signed-radical-kernel';base=Path('rounds/codex-managed')/cid
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
start=read(base/'controls/starting_state_hashes.json')
assert all(sha(p)==h for p,h in start.items())
for p,h in read(base/'controls/frozen_artifact_hashes.json').items():assert sha(p)==h,('frozen',p)
prior_entries=[e for e in read('state/round_ledger.yml')['rounds'] if 200<=e['round_index']<=217]
assert len(prior_entries)==18 and all(e['status']=='closed' for e in prior_entries)
archive_count=0
for e in prior_entries:
 for p,h in read(Path('rounds/codex-managed')/e['campaign_id']/'controls/artifact_hashes.json').items():
  assert sha(p)==h,('prior archive',p);archive_count+=1
assert archive_count==433,archive_count
raw_graph=gp.read_bytes();raw_draft=draft.read_bytes();g=load_graph(gp)
assert len(g['proof_obligations'])==401 and not validate_graph(g,root=root)
m=read('state/active_campaign.yml')
assert m['round_index']==218 and m['campaign_id']==cid and m['status']=='active'
assert not validate_campaign(m,g,root=root)
frozen=read(base/'plan.json')['campaign']
for key in ['frozen_target','completion_criteria','resource_policy','controls','target_obligations','review_seams']:assert m[key]==frozen[key],key
assert len(m['tasks'])==len(frozen['tasks'])==3
for t,f in zip(m['tasks'],frozen['tasks']):
 assert {k:v for k,v in t.items() if k!='status'}=={k:v for k,v in f.items() if k!='status'}
 contract(t['report_path'])
fixed={
 'reports/joint_divisor_kernel.md':'81a983cbf4f3de82e0c88911d1569c26b3920c7b6cb4adaf7ebb71918cdcba87',
 'reports/joint_lattice_kernel.md':'c3193b053d594b3a1599cdf707161b438f3387703f9e0f2010cf1d3b0101d41c',
 'reports/blind_joint_radial.md':'339971305a6dd5af4460d8827cb920c75350531294021b50df8c9249be062a47',
 'controls/conductor_joint_rank_and_shell_cost.md':'f865b9d69883b47d75cb1033b3aaf3f4a1ee9e6a9015ae5deb42f76eed570b2d',
 'reviews/independent_joint_lattice_review.md':'502ed99070c1d474ab4139deaea50edd498692ab557a93f4b7aea5d764cbbe50',
 'reviews/independent_joint_divisor_and_control_review.md':'11f1d2d3ee482ae3fb1ba1c201afed9b9f58c671986e4a1bb52ed6fb841ecbd7',
 'reviews/isolated_packet_coherence_rederivation.md':'bec8ef06ba0a0105bf0cf07feb2ed2bacb301d7958a7b41e42276d02ffd73f1e',
}
for rel,h in fixed.items():assert sha(base/rel)==h,('final hash',rel)
power=base/'controls/conductor_joint_rank_and_shell_cost.md';contract(power)
packet=base/'briefs/isolated_packet_coherence_statement.md'
isolated=base/'reviews/isolated_packet_coherence_rederivation.md'
assert sha(packet) in contract(isolated).lower()
assert 'not a fresh history-free agent' in contract(base/'reports/blind_joint_radial.md')
dispatch=read(base/'controls/dispatch_provenance.json')
assert dispatch['frozen_objective_changed'] is False
reviews=[
 (base/'reviews/conductor_joint_radial_review.md',[base/'reports/blind_joint_radial.md']),
 (base/'reviews/independent_joint_lattice_review.md',[base/'reports/joint_lattice_kernel.md']),
 (base/'reviews/independent_joint_divisor_and_control_review.md',[base/'reports/joint_divisor_kernel.md',power]),
 (isolated,[packet]),
 (base/'reviews/conductor_packet_coherence_binding.md',[isolated,base/'reports/joint_lattice_kernel.md']),
]
for p,arts in reviews:
 s=contract(p);assert 'GREEN' in s,p
 assert 'PACKET_REPORT_HASH' not in s
 for a in arts:assert sha(a) in s.lower(),('review binding',p,a)
decision=read(base/'controls/closing_decision.json')
assert decision['graph_mutation'] is False and not decision['pointwise_exponent_change'] and not decision['complete_moment_bound_improved']
contract(base/'synthesis.md')
evidence=[Path(t['report_path']) for t in m['tasks']]+[power,packet]+[p for p,_ in reviews]+[base/'controls/dispatch_provenance.json',base/'synthesis.md']
judge=base/'reviews/conductor_round218_reconciliation.md';s=contract(judge)
bindings='\n'.join(f'- `{p.as_posix()}`: `{sha(p)}`.' for p in evidence)
if 'FINAL_HASH_BINDINGS' in s:put(judge,s.replace('FINAL_HASH_BINDINGS',bindings).encode())
else:assert bindings in s
assert 'GREEN for the scoped joint-transform diagnoses only' in contract(judge)
hygiene=[]
for p in base.rglob('*.md'):
 raw=p.read_bytes();s=raw.decode();assert not re.search(rb'\r(?!\n)',raw),p
 assert '\ufffd' not in s and not any(ord(c)<32 and c not in '\n\r\t' for c in s),p
 hygiene.append(p.as_posix())
protected=['GC-target','Conditional-bridge','M9','M9-M1','M9-M2','M9-endpoint-uniformity',
 'GC-external-Li-Yang-theta-star','GC-weighted-square-root-exact-resonance-mass',
 'GC-complete-square-root-large-values-moment-bound','GC-complete-distinct-radical-twelfth-reduction',
 'GC-distinct-radical-absolute-certificate-obstruction']
patch=dict(round_index=218,campaign_id=cid,starting_graph_sha256=start[gp.as_posix()],
 proof_obligations=dict(create=[],update=[],correct_rejected=[],reject=[],no_change=protected),
 round_assessment=dict(terminal_label=decision['terminal_label'],reason=decision['reason']),
 reversibility=dict(rule='Identity in-memory application, inverse and replay; graph and proof-draft bytes are never rewritten.'))
assert not validate_patch_against_graph(g,patch)
applied,result=apply_state_patch(copy.deepcopy(g),patch,round_index=218,judge_ref=judge.as_posix())
assert applied==g and not any([result.created,result.updated,result.rejected,result.corrected_rejected])
inverse=copy.deepcopy(applied)
replay,_=apply_state_patch(copy.deepcopy(inverse),patch,round_index=218,judge_ref=judge.as_posix())
assert inverse==g and replay==g and dump_graph(replay)==dump_graph(g)
write(base/'state_patch.json',patch)
preflight=dict(round_index=218,status='green_identity_patch_preflight',graph_schema='pass',campaign_schema='pass',identity_patch='pass',reverse_identity_replay='pass',
 all_401_nodes_and_other_graph_data_unchanged=True,exact_review_hashes={a.as_posix():sha(a) for _,arts in reviews for a in arts},
 three_report_hashes={t['report_path']:sha(t['report_path']) for t in m['tasks']},frozen_scope_and_briefs_unchanged=True,
 closed_round200_through217_archives_unchanged=True,protected_archive_entries_checked=archive_count,report_hygiene=hygiene,
 mathematical_numerical_experiments=0,analytical_algebraic_percent_at_least=95,analytic_target='open',complete_moment_bound_improved=False,pointwise_exponent_change=False)
write(base/'controls/closure_preflight.json',preflight)
assert not subprocess.check_output(['git','diff','--name-only','--','rounds/obligation-main','rounds/web-research-test']).strip()
subprocess.run(['git','diff','--check'],check=True)
matrix=read('state/validation_matrix.yml')
oldgates=copy.deepcopy([x for x in matrix['gates'] if not x['id'].startswith('round218_')])
for gate in matrix['gates']:
 if gate['id'].startswith('round218_'):gate['status']='green_scoped_evidence_actual_target_open'
for review,_ in reviews:matrix['gates'].append(dict(id='round218_'+review.stem,status='green',artifact=review.as_posix()))
matrix['gates'].append(dict(id='round218_identity_patch_scope',status='green',artifact=(base/'controls/closure_preflight.json').as_posix()))
round_gates=[x for x in matrix['gates'] if x['id'].startswith('round218_')]
assert len(round_gates)==10 and all(x['status'].startswith('green') and Path(x['artifact']).is_file() for x in round_gates)
assert oldgates==[x for x in matrix['gates'] if not x['id'].startswith('round218_')]
matrix.update(promotion_status='round_218_closed_identity_patch_complete_joint_kernel_diagnosis',graph_sha256=sha(gp),analytic_target_status='open_complete_actual_signed_twelfth_moment',
 decision_rule='Reviewed complete joint-transform costs and qualified certificate no-go only. All401 nodes and accepted powers unchanged. Next219 pending design; broad review220.')
write('state/validation_matrix.yml',matrix)
assert gp.read_bytes()==raw_graph and draft.read_bytes()==raw_draft and all(sha(p)==h for p,h in start.items())
assessment=dict(decision=decision['decision'],terminal_label=decision['terminal_label'],graph_mutation=False,
 main_result=decision['reason'],resulting_graph_sha256=sha(gp),patch_effect=f'0_create_0_update_0_correct_0_reject_{len(protected)}_no_change',
 complete_moment_bound_improved=False,pointwise_exponent_change=False,goal_turn_classification=decision['goal_turn_classification'])
m.update(status='complete',completed_at=now,closing_assessment=assessment,post_report_reviews=[p.as_posix() for p,_ in reviews],conductor_interventions=decision['interventions'])
for t in m['tasks']:t['status']='completed'
assert not validate_campaign(m,g,root=root);write('state/active_campaign.yml',m)
lp=Path('state/round_ledger.yml');ledger_raw=lp.read_bytes();s=ledger_raw.decode();ledger=json.loads(s)
assert ledger['active_round']==218 and ledger['rounds'][-1]['round_index']==218
oldentries=copy.deepcopy(ledger['rounds'][:-1]);entry=ledger['rounds'][-1]
entry.update(status='closed',closing_assessment=assessment,completed_at=now,next_round=219)
for t in entry['tasks']:t['status']='completed'
matches=list(re.finditer(r'    \{\r?\n      "round_index": 218,',s));assert len(matches)==1
pos=matches[0].start();eol='\r\n' if '\r\n' in s else '\n'
new=s[:pos]+eol.join('    '+line for line in json.dumps(entry,indent=2,ensure_ascii=False).splitlines())+eol+'  ]'+eol+'}'+eol
assert json.loads(new)==ledger and ledger['rounds'][:-1]==oldentries
assert new[:pos].encode()==ledger_raw[:len(s[:pos].encode())];put(lp,new.encode())
write('state/next_round_plan.yml',dict(round_index=219,status='pending_design',campaign_id=None,tasks=[],starting_graph_sha256=sha(gp),predecessor_round=218,
 predecessor_terminal_label=decision['terminal_label'],candidate_objective=decision['next_objective'],candidate_method=decision['next_method'],
 first_unproved_estimate=decision['first_unproved_estimate'],exact_closed_dependencies=[p.as_posix() for p in evidence]+[judge.as_posix(),
 'strategy/gauss_circle_strategy_checkpoint_round217_2026-09-28.md','rounds/codex-managed/gc-actual-radical-high-values/reports/anchored_divisor_high_values.md'],
 design_constraint='Preserve one complete actual signed target. Require a genuinely joint arithmetic mechanism; no repeat of stationary-rank heuristics, odd-profile centering or absolute dual-tuple closure under either placement of the modulus.',
 full_goal_scope='Quarter remains open. A fixed twelfth milestone is insufficient; the unbounded-fixed-order family and every full M1/M2/GAR frontier remain as in checkpoint217.',
 scheduled_review='Mandatory broad strategy/current-primary-literature review220 after217--219.',prior_turn_classification=assessment['goal_turn_classification']))
summary=_next_campaign(m,output_dir=base,graph_hash=sha(gp))+'\n## Closing decision\n\nRound218 closed with complete joint-transform diagnoses and a qualified after-radius absolute-certificate no-go. Identity State Patch; all401 nodes and graph/draft bytes unchanged. No improved complete moment or exponent. Next219 pending design; broad review220.\n'
for p in ['state/current_round.md','state/next_campaign.md']:put(p,summary.encode())
note='\n## Round218 complete joint signed-kernel attack (2026-09-28)\n\n'+decision['state_note']+'\n'
for p in ['state/project_summary.md','state/current_state.md','state/failure_ledger.md']:
 raw=Path(p).read_bytes();assert b'## Round218 complete joint signed-kernel attack' not in raw;put(p,raw+note.encode())
assert all(sha(p)==h for p,h in start.items())
validation=dict(preflight,campaign_id=cid,generated_at=now,terminal_label=decision['terminal_label'],starting_graph_sha256=start[gp.as_posix()],
 final_graph_sha256=sha(gp),canonical_graph_sha256=hashlib.sha256(dump_graph(g).encode()).hexdigest(),graph_nodes=401,
 original_graph_raw_bytes_unchanged=True,proof_draft_raw_bytes_unchanged=True,final_proof_draft_sha256=sha(draft),
 previous_ledger_prefix_bytes_unchanged=True,legacy_paths_unchanged=True,next_strategy_checkpoint=220,green_round_gates=len(round_gates))
validation['status']='green_round218_complete_joint_kernel_closure_no_complete_moment_gain'
write(base/'controls/closure_validation.json',validation)
vtext=f'''# Round218 closure validation

GREEN for the complete joint-transform diagnosis and specified positive certificates only.
Actual signed I12, complete dual moment and full quarter theorem remain OPEN.
Graph SHA256:{sha(gp)}. Identity patch validated/applied in memory/reversed/replayed;
all401 nodes, graph/draft bytes and previous ledger prefix unchanged. Three frozen
reports, exact-hash cross-reviews, two statement-only derivations and conductor
actual bindings passed. All10 required round gates green. All433 prior archive
entries and frozen218 inputs verified unchanged. Reviewer prior-context reuse
is explicitly disclosed; no fresh-history claim is made. Zero numerical experiments
and no new external theorem import. No complete moment or exponent improvement.
These checks do not reprove historical mathematics. Next219 pending design;
next mandatory broad strategy/current-literature review220.
Details:{base.as_posix()}/controls/closure_validation.json.
'''
for p in ['state/last_validation.md','state/last_validation_report.md']:put(p,vtext.encode())
assert not validate_graph(load_graph(gp),root=root) and not validate_campaign(read('state/active_campaign.yml'),g,root=root)
assert not subprocess.check_output(['git','diff','--name-only','--','rounds/obligation-main','rounds/web-research-test']).strip()
subprocess.run(['git','diff','--check'],check=True)
hashes={p.relative_to(root).as_posix():sha(p) for p in sorted((root/base).rglob('*')) if p.is_file() and p.name!='artifact_hashes.json' and '__pycache__' not in p.parts}
strategy=Path('strategy/round218_complete_signed_radical_kernel.md');hashes[strategy.as_posix()]=sha(strategy)
write(base/'controls/artifact_hashes.json',hashes)
print(json.dumps({k:validation[k] for k in ['status','graph_nodes','final_graph_sha256','proof_draft_raw_bytes_unchanged',
 'green_round_gates','protected_archive_entries_checked','pointwise_exponent_change']},indent=2))
