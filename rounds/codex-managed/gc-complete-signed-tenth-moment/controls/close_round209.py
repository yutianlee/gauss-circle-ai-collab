"""Close round209 only after all final reports and seam hashes pass."""
import copy,hashlib,json,re,subprocess,sys,time
from datetime import datetime,timezone
from pathlib import Path
root=Path.cwd();sys.path.insert(0,str(root))
from math_collab.campaigns import validate_campaign,_next_campaign
from math_collab.proof_obligations import load_graph,dump_graph,validate_graph,validate_patch_against_graph,apply_state_patch
cid='gc-complete-signed-tenth-moment';base=Path('rounds/codex-managed')/cid
gp=Path('state/proof_obligations.yml');now=datetime.now(timezone.utc).isoformat()
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
 s=Path(p).read_text(encoding='utf-8');assert all(re.search(rf'^#{{1,2}} {i}\.',s,re.M) for i in range(1,8)),p;return s
start=read(base/'controls/starting_state_hashes.json')
assert all(sha(p)==h for p,h in start.items())
for p,h in read(base/'controls/frozen_artifact_hashes.json').items():assert sha(p)==h,('frozen',p)
priors=['m9-m1-t1-complete-source-coefficient-mask-analysis','gc-whole-discrepancy-twelfth-moment',
'gc-strategy-signed-moment-majorant-review','gc-complete-signed-convolution-attack','gc-complete-large-values-duality',
'gc-full-frontier-moment-strategy-review','gc-complete-signed-shell-arithmetic','gc-signed-rational-filter-attack','gc-full-proof-signed-arithmetic-review']
archive_count=0
for prior in priors:
 for p,h in read(Path('rounds/codex-managed')/prior/'controls/artifact_hashes.json').items():assert sha(p)==h,('archive',p);archive_count+=1
raw_graph=gp.read_bytes();g=load_graph(gp);assert len(g['proof_obligations'])==399 and not validate_graph(g,root=root)
m=read('state/active_campaign.yml');assert m['round_index']==209 and m['campaign_id']==cid and m['status']=='active'
assert not validate_campaign(m,g,root=root)
frozen=read(base/'plan.json')['campaign']
for key in ['frozen_target','completion_criteria','resource_policy','controls','target_obligations','review_seams']:assert m[key]==frozen[key],key
for t,f in zip(m['tasks'],frozen['tasks']):
 assert {k:v for k,v in t.items() if k!='status'}=={k:v for k,v in f.items() if k!='status'}
 contract(t['report_path'])
assert len(m['tasks'])==len(frozen['tasks'])==3
power=base/'controls/conductor_tenth_power_ledger.md';contract(power)
reviews=[
 (base/'reviews/independent_tenth_power_review.md',[power]),
 (base/'reviews/independent_rational_tenth_review.md',[base/'reports/signed_fifth_convolution.md']),
 (base/'reviews/independent_high_values_review.md',[base/'reports/actual_tenth_high_values.md']),
 (base/'reviews/conductor_blind_report_review.md',[base/'reports/blind_ten_root_audit.md'])]
for p,arts in reviews:
 s=contract(p);assert 'GREEN' in s,p
 for a in arts:assert sha(a) in s.lower(),('review binding',p,a)
decision=read(base/'controls/closing_decision.json');assert decision['graph_mutation'] is False and decision['pointwise_exponent_change'] is False
assert (base/'synthesis.md').is_file()
evidence=[Path(t['report_path']) for t in m['tasks']]+[power]+[p for p,_ in reviews]
judge=base/'reviews/conductor_round209_reconciliation.md';s=contract(judge);assert 'FINAL_HASH_BINDINGS' in s
put(judge,s.replace('FINAL_HASH_BINDINGS','\n'.join(f'- `{p.as_posix()}`: `{sha(p)}`.' for p in evidence)).encode())
hygiene=[]
for p in base.rglob('*.md'):
 raw=p.read_bytes();s=raw.decode();assert not re.search(rb'\r(?!\n)',raw),p
 assert '\ufffd' not in s and not any(ord(c)<32 and c not in '\n\r\t' for c in s),p
 hygiene.append(p.as_posix())
protected=['GC-target','Conditional-bridge','M9','M9-M1','M9-M2','M9-endpoint-uniformity','GC-external-Li-Yang-theta-star',
'GC-weighted-square-root-exact-resonance-mass','GC-physical-twelfth-moment-absolute-majorant-obstruction','GC-complete-square-root-large-values-moment-bound']
patch=dict(round_index=209,campaign_id=cid,starting_graph_sha256=start[gp.as_posix()],
proof_obligations=dict(create=[],update=[],correct_rejected=[],reject=[],no_change=protected),
round_assessment=dict(terminal_label=decision['terminal_label'],reason=decision['reason']),
reversibility=dict(rule='Identity in-memory application, inverse and replay; graph/draft bytes never rewritten.'))
assert not validate_patch_against_graph(g,patch)
applied,result=apply_state_patch(copy.deepcopy(g),patch,round_index=209,judge_ref=judge.as_posix())
assert applied==g and not any([result.created,result.updated,result.rejected,result.corrected_rejected])
inverse=copy.deepcopy(applied);replay,_=apply_state_patch(copy.deepcopy(inverse),patch,round_index=209,judge_ref=judge.as_posix())
assert inverse==g and replay==g and dump_graph(replay)==dump_graph(g)
write(base/'state_patch.json',patch)
preflight=dict(round_index=209,status='green_identity_patch_preflight',graph_schema='pass',campaign_schema='pass',identity_patch='pass',reverse_identity_replay='pass',
all_399_nodes_and_other_graph_data_unchanged=True,exact_review_hashes={a.as_posix():sha(a) for _,arts in reviews for a in arts},
three_report_hashes={t['report_path']:sha(t['report_path']) for t in m['tasks']},frozen_scope_and_briefs_unchanged=True,
closed_round200_through208_archives_unchanged=True,protected_archive_entries_checked=archive_count,report_hygiene=hygiene,
mathematical_numerical_experiments=0,analytic_target='open',complete_moment_bound_improved=False,pointwise_exponent_change=False)
write(base/'controls/closure_preflight.json',preflight)
matrix=read('state/validation_matrix.yml');oldgates=copy.deepcopy([x for x in matrix['gates'] if not x['id'].startswith('round209_')])
for gate in matrix['gates']:
 if gate['id'].startswith('round209_'):gate['status']='green_scoped_evidence_actual_target_open'
for review,_ in reviews:matrix['gates'].append(dict(id='round209_'+review.stem,status='green',artifact=review.as_posix()))
matrix['gates'].append(dict(id='round209_identity_patch_scope',status='green',artifact=(base/'controls/closure_preflight.json').as_posix()))
assert all(x['status'].startswith('green') and Path(x['artifact']).is_file() for x in matrix['gates'] if x['id'].startswith('round209_'))
assert oldgates==[x for x in matrix['gates'] if not x['id'].startswith('round209_')]
matrix.update(promotion_status='round_209_closed_identity_patch_scoped_arithmetic_diagnostics',graph_sha256=sha(gp),analytic_target_status='open_complete_signed_block_tenth_moment',decision_rule='Scoped reviewed bounds and no-go only. Actual K10 and full quarter open.210 pending design; next review211.')
write('state/validation_matrix.yml',matrix)
assert gp.read_bytes()==raw_graph and all(sha(p)==h for p,h in start.items())
assessment=dict(decision='retain_graph_record_reviewed_arithmetic_diagnostics',terminal_label=decision['terminal_label'],graph_mutation=False,
main_result=decision['reason'],resulting_graph_sha256=sha(gp),patch_effect='0_create_0_update_0_correct_0_reject_10_no_change',
complete_moment_bound_improved=False,pointwise_exponent_change=False,goal_turn_classification=decision['goal_turn_classification'])
m.update(status='complete',completed_at=now,closing_assessment=assessment,post_report_reviews=[p.as_posix() for p,_ in reviews],conductor_interventions=decision['interventions'])
for t in m['tasks']:t['status']='completed'
assert not validate_campaign(m,g,root=root);write('state/active_campaign.yml',m)
lp=Path('state/round_ledger.yml');ledger_raw=lp.read_bytes();s=ledger_raw.decode();ledger=json.loads(s)
assert ledger['active_round']==209 and ledger['rounds'][-1]['round_index']==209
oldentries=copy.deepcopy(ledger['rounds'][:-1]);entry=ledger['rounds'][-1]
entry.update(status='closed',closing_assessment=assessment,completed_at=now,next_round=210)
for t in entry['tasks']:t['status']='completed'
matches=list(re.finditer(r'    \{\r?\n      "round_index": 209,',s));assert len(matches)==1;pos=matches[0].start();eol='\r\n' if '\r\n' in s else '\n'
new=s[:pos]+eol.join('    '+line for line in json.dumps(entry,indent=2,ensure_ascii=False).splitlines())+eol+'  ]'+eol+'}'+eol
assert json.loads(new)==ledger and json.loads(new)['rounds'][:-1]==oldentries
assert new[:pos].encode()==ledger_raw[:len(s[:pos].encode())];put(lp,new.encode())
write('state/next_round_plan.yml',dict(round_index=210,status='pending_design',campaign_id=None,starting_graph_sha256=sha(gp),predecessor_round=209,
predecessor_terminal_label=decision['terminal_label'],tasks=[],candidate_objective=decision['next_objective'],candidate_method=decision['next_method'],
first_unproved_estimate=decision['first_unproved_estimate'],exact_closed_dependencies=[p.as_posix() for p in evidence]+[judge.as_posix(),(base/'synthesis.md').as_posix()],
design_constraint='Design only from closed209. No more exact-diagonal optimization, new identities alone, or termwise absolute near-frequency closure; preserve all complements and both known deficits.',
full_goal_scope='The102/325 milestone is not the quarter theorem. Full quarter still requires arbitrarily high fixed moment/peak gates and verified bands, or complete alternative parents. M1/M2 remain open.',
scheduled_review='Next broad strategy/current-literature review211 after208--210.',prior_turn_classification=assessment['goal_turn_classification']))
summary=_next_campaign(m,output_dir=base,graph_hash=sha(gp))+'\n## Closing decision\n\nRound209 closed with reviewed scoped arithmetic diagnostics, identity State Patch, no complete moment or exponent gain.210 pending design; next broad review211.\n'
for p in ['state/current_round.md','state/next_campaign.md']:put(p,summary.encode())
note='\n## Round209 complete signed tenth-moment attack (2026-09-27)\n\n'+decision['state_note']+'\n'
for p in ['state/project_summary.md','state/current_state.md','state/failure_ledger.md']:
 raw=Path(p).read_bytes();assert b'## Round209 complete signed tenth-moment attack' not in raw;put(p,raw+note.encode())
assert not subprocess.check_output(['git','diff','--name-only','--','rounds/obligation-main','rounds/web-research-test']).strip()
assert all(sha(p)==h for p,h in start.items())
validation=dict(preflight,campaign_id=cid,generated_at=now,terminal_label=decision['terminal_label'],starting_graph_sha256=start[gp.as_posix()],
final_graph_sha256=sha(gp),canonical_graph_sha256=hashlib.sha256(dump_graph(g).encode()).hexdigest(),graph_nodes=399,
original_graph_raw_bytes_unchanged=True,proof_draft_raw_bytes_unchanged=True,previous_ledger_prefix_bytes_unchanged=True,legacy_paths_unchanged=True,next_strategy_checkpoint=211)
validation['status']='green_round209_scoped_arithmetic_closure_no_complete_moment_or_exponent_gain'
write(base/'controls/closure_validation.json',validation)
vtext=f'''# Round209 closure validation

GREEN for scoped arithmetic bounds, method no-go results and state closure only.
Actual complete tenth-moment target and full quarter theorem remain OPEN.
Graph SHA256:{sha(gp)}. Identity patch validated/applied in memory/reversed/replayed;
all399 graph nodes, graph/draft bytes and previous ledger prefix unchanged. Three
reports, three independent seam reviews and conductor blind-report review passed
at final hashes. Round200--208 archives and frozen209 inputs verified unchanged.
No complete moment or pointwise improvement; no mathematical numerical experiments.
Schema checks do not reprove historical mathematics.210 pending design; review211.
Details:{base.as_posix()}/controls/closure_validation.json.
'''
for p in ['state/last_validation.md','state/last_validation_report.md']:put(p,vtext.encode())
assert not validate_graph(load_graph(gp),root=root) and not validate_campaign(read('state/active_campaign.yml'),g,root=root)
subprocess.run(['git','diff','--check'],check=True)
hashes={p.relative_to(root).as_posix():sha(p) for p in sorted((root/base).rglob('*')) if p.is_file() and p.name!='artifact_hashes.json' and '__pycache__' not in p.parts}
strategy=Path('strategy/round209_complete_signed_tenth_moment_attack.md');hashes[strategy.as_posix()]=sha(strategy)
write(base/'controls/artifact_hashes.json',hashes)
print(json.dumps({k:validation[k] for k in ['status','graph_nodes','final_graph_sha256','proof_draft_raw_bytes_unchanged','pointwise_exponent_change']},indent=2))
