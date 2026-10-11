"""Close220 once after the final mathematical/source reviews. Never rerun."""
import copy, hashlib, json, re, subprocess, sys, time
from pathlib import Path
from datetime import datetime, timezone
root=Path.cwd(); sys.path.insert(0,str(root))
from math_collab.campaigns import validate_campaign, _next_campaign
from math_collab.proof_obligations import load_graph, dump_graph, validate_graph, validate_patch_against_graph, apply_state_patch
cid='gc-full-goal-arithmetic-source-review'; base=Path('rounds/codex-managed')/cid
gp=Path('state/proof_obligations.yml'); draft=Path('state/best_proof_draft.md')
checkpoint=Path('strategy/gauss_circle_strategy_checkpoint_round220_2026-09-28.md')
now=datetime.now(timezone.utc).isoformat()
def read(p): return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def put(p,b):
    for i in range(5):
        try: Path(p).write_bytes(b); return
        except OSError:
            if i==4: raise
            time.sleep(.2)
def write(p,o): put(p,(json.dumps(o,indent=2,ensure_ascii=False)+'\n').encode())
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def contract(p):
    s=Path(p).read_text(encoding='utf-8')
    assert all(re.search(rf'^#{{1,2}} {i}\.',s,re.M) for i in range(1,8)),p
    return s
m=read('state/active_campaign.yml')
assert m['round_index']==220 and m['status']=='active' and m['campaign_id']==cid
assert not (base/'controls/artifact_hashes.json').exists(), 'Already archived; do not rerun'
start=read(base/'controls/starting_state_hashes.json')
assert all(sha(p)==h for p,h in start.items())
for p,h in read(base/'controls/frozen_artifact_hashes.json').items(): assert sha(p)==h,('frozen',p)
entries=[e for e in read('state/round_ledger.yml')['rounds'] if 200<=e['round_index']<=219]
assert len(entries)==20 and all(e['status']=='closed' for e in entries)
count=0
for e in entries:
    for p,h in read(Path('rounds/codex-managed')/e['campaign_id']/'controls/artifact_hashes.json').items():
        assert sha(p)==h,('closed archive',p); count+=1
assert count==488
raw_graph=gp.read_bytes(); raw_draft=draft.read_bytes(); g=load_graph(gp)
assert len(g['proof_obligations'])==401 and not validate_graph(g,root=root)
assert not validate_campaign(m,g,root=root)
frozen=read(base/'plan.json')['campaign']
for key in ['frozen_target','completion_criteria','resource_policy','controls','target_obligations','review_seams']: assert m[key]==frozen[key]
assert len(m['tasks'])==len(frozen['tasks'])==3
for t,f in zip(m['tasks'],frozen['tasks']):
    assert {k:v for k,v in t.items() if k!='status'}=={k:v for k,v in f.items() if k!='status'}
    contract(t['report_path'])
for p,h in read(base/'controls/final_evidence_hashes.json').items(): assert sha(p)==h,('final evidence',p)
assert 'not a fresh history-free agent' in contract(base/'reports/blind_smooth_mask.md')
assert read(base/'controls/dispatch_provenance.json')['frozen_objective_changed'] is False
control=base/'controls/conductor_rounding_and_operator_control.md'
status=base/'controls/conductor_current_source_status.md'
correction=base/'controls/conductor_frontier_normalization_correction.md'
packet=base/'briefs/blind_smooth_mask_statement.md'
for p in [control,status,correction]: contract(p)
reviews=[
    (base/'reviews/conductor_smooth_mask_review.md',[base/'reports/blind_smooth_mask.md',packet]),
    (base/'reviews/independent_rounding_application_review.md',[control]),
    (base/'reviews/independent_reciprocal_source_review.md',[base/'reports/reciprocal_energy_sources.md']),
    (base/'reviews/independent_full_frontier_source_review.md',[base/'reports/full_frontier_sources.md']),
    (base/'reviews/conductor_source_and_strategy_review.md',[base/'reports/reciprocal_energy_sources.md',base/'reports/full_frontier_sources.md',status,correction,checkpoint]),
]
for p,arts in reviews:
    s=contract(p); assert 'GREEN' in s,p
    for a in arts: assert sha(a) in s.lower(),('review binding',p,a)
decision=read(base/'controls/closing_decision.json')
assert decision['graph_mutation'] is False and not decision['complete_moment_bound_improved'] and not decision['pointwise_exponent_change']
assert decision['terminal_label'] in m['exit_labels']
contract(base/'synthesis.md')
evidence=[Path(t['report_path']) for t in m['tasks']]+[control,status,correction,packet,checkpoint]+[p for p,_ in reviews]+[base/'controls/dispatch_provenance.json',base/'synthesis.md']
judge=base/'reviews/conductor_round220_reconciliation.md'; s=contract(judge)
bindings='\n'.join(f'- `{p.as_posix()}`: `{sha(p)}`.' for p in evidence)
assert 'FINAL_HASH_BINDINGS' in s
put(judge,s.replace('FINAL_HASH_BINDINGS',bindings).encode())
assert 'GREEN for scoped source and operator evidence only' in contract(judge)
for p in list(base.rglob('*.md'))+[checkpoint]:
    raw=p.read_bytes(); s=raw.decode(); assert not re.search(rb'\r(?!\n)',raw),p
    assert '\ufffd' not in s and not any(ord(c)<32 and c not in '\n\r\t' for c in s),p
protected=['GC-target','Conditional-bridge','M9','M9-M1','M9-M2','M9-endpoint-uniformity','M9-M2-smooth-unbalanced-three-quarter-estimate','GC-external-Li-Yang-theta-star','GC-weighted-square-root-exact-resonance-mass','GC-complete-square-root-large-values-moment-bound','GC-complete-distinct-radical-twelfth-reduction','GC-distinct-radical-absolute-certificate-obstruction']
patch=dict(round_index=220,campaign_id=cid,starting_graph_sha256=start[gp.as_posix()],proof_obligations=dict(create=[],update=[],correct_rejected=[],reject=[],no_change=protected),round_assessment=dict(terminal_label=decision['terminal_label'],reason=decision['reason']),reversibility=dict(rule='Identity in-memory application, inverse and replay; graph and proof-draft bytes never rewritten.'))
assert not validate_patch_against_graph(g,patch)
applied,result=apply_state_patch(copy.deepcopy(g),patch,round_index=220,judge_ref=judge.as_posix())
assert applied==g and not any([result.created,result.updated,result.rejected,result.corrected_rejected])
replay,_=apply_state_patch(copy.deepcopy(applied),patch,round_index=220,judge_ref=judge.as_posix())
assert replay==g and dump_graph(replay)==dump_graph(g)
write(base/'state_patch.json',patch)
preflight=dict(round_index=220,status='green_identity_patch_preflight',graph_schema='pass',campaign_schema='pass',identity_patch='pass',reverse_identity_replay='pass',all_401_nodes_unchanged=True,frozen_scope_and_briefs_unchanged=True,protected_archive_entries_checked=count,closed_round200_through219_archives_unchanged=True,mathematical_numerical_experiments=0,analytical_algebraic_percent_at_least=95,complete_moment_bound_improved=False,pointwise_exponent_change=False)
write(base/'controls/closure_preflight.json',preflight)
assert not subprocess.check_output(['git','diff','--name-only','--','rounds/obligation-main','rounds/web-research-test']).strip()
subprocess.run(['git','diff','--check'],check=True)
matrix=read('state/validation_matrix.yml'); prior=copy.deepcopy([x for x in matrix['gates'] if not x['id'].startswith('round220_')])
for gate in matrix['gates']:
    if gate['id'].startswith('round220_'): gate['status']='green_scoped_evidence_actual_target_open'
for p,_ in reviews: matrix['gates'].append(dict(id='round220_'+p.stem,status='green',artifact=p.as_posix()))
matrix['gates'].append(dict(id='round220_identity_patch_scope',status='green',artifact=(base/'controls/closure_preflight.json').as_posix()))
gates=[x for x in matrix['gates'] if x['id'].startswith('round220_')]
assert len(gates)==10 and all(x['status'].startswith('green') and Path(x['artifact']).is_file() for x in gates)
assert prior==[x for x in matrix['gates'] if not x['id'].startswith('round220_')]
matrix.update(promotion_status='round_220_closed_identity_patch_no_complete_source_gain',graph_sha256=sha(gp),analytic_target_status='open_complete_actual_signed_twelfth_moment',decision_rule='Exact current-source costs and smooth-mask lemma reviewed. No complete gain. Strategy checkpoint220 supersedes the erroneous217 UNBAL summary row; graph unchanged.')
write('state/validation_matrix.yml',matrix)
assert gp.read_bytes()==raw_graph and draft.read_bytes()==raw_draft
assessment=dict(decision=decision['decision'],terminal_label=decision['terminal_label'],graph_mutation=False,main_result=decision['reason'],resulting_graph_sha256=sha(gp),patch_effect=f'0_create_0_update_0_correct_0_reject_{len(protected)}_no_change',complete_moment_bound_improved=False,pointwise_exponent_change=False,goal_turn_classification=decision['goal_turn_classification'])
m.update(status='complete',completed_at=now,closing_assessment=assessment,post_report_reviews=[p.as_posix() for p,_ in reviews],conductor_interventions=decision['interventions'])
for t in m['tasks']: t['status']='completed'
assert not validate_campaign(m,g,root=root); write('state/active_campaign.yml',m)
lp=Path('state/round_ledger.yml'); ledger_raw=lp.read_bytes(); s=ledger_raw.decode(); ledger=json.loads(s)
assert ledger['active_round']==220 and ledger['rounds'][-1]['round_index']==220
oldentries=copy.deepcopy(ledger['rounds'][:-1]); entry=ledger['rounds'][-1]
entry.update(status='closed',closing_assessment=assessment,completed_at=now,next_round=221)
for t in entry['tasks']: t['status']='completed'
matches=list(re.finditer(r'    \{\r?\n      "round_index": 220,',s)); assert len(matches)==1
pos=matches[0].start(); eol='\r\n' if '\r\n' in s else '\n'
new=s[:pos]+eol.join('    '+line for line in json.dumps(entry,indent=2,ensure_ascii=False).splitlines())+eol+'  ]'+eol+'}'+eol
assert json.loads(new)==ledger and ledger['rounds'][:-1]==oldentries
assert new[:pos].encode()==ledger_raw[:len(s[:pos].encode())]; put(lp,new.encode())
write('state/next_round_plan.yml',dict(round_index=221,status='pending_design',campaign_id=None,tasks=[],starting_graph_sha256=sha(gp),predecessor_round=220,predecessor_terminal_label=decision['terminal_label'],candidate_objective=decision['next_objective'],candidate_method=decision['next_method'],first_unproved_estimate=decision['first_unproved_estimate'],exact_closed_dependencies=[p.as_posix() for p in evidence]+[judge.as_posix()],design_constraint='Design only from closed220. Retain complete actual signed scope, all coefficient norms, aliases and complements; no automatic source import or enlarged coefficient grant.',full_goal_scope='Quarter, sufficient unbounded fixed-order family and all complete M1/M2/GAR frontiers remain open.',scheduled_review='Next broad strategy/current-primary-literature review223 after220--222.',prior_turn_classification=assessment['goal_turn_classification']))
summary=_next_campaign(m,output_dir=base,graph_hash=sha(gp))+'\n## Closing decision\n\nRound220 closed with exact current-source cost audits and the smooth-mask lemma. Identity State Patch; all401 nodes and proof-draft bytes unchanged. No improved complete energy, moment or exponent. Checkpoint220 corrects the earlier UNBAL summary. Round221 pending design; broad review223 next.\n'
for p in ['state/current_round.md','state/next_campaign.md']: put(p,summary.encode())
note='\n## Round220 full-goal strategy and current-source review (2026-09-28)\n\n'+decision['state_note']+'\n'
for p in ['state/project_summary.md','state/current_state.md','state/failure_ledger.md']:
    raw=Path(p).read_bytes(); assert b'## Round220 full-goal strategy and current-source review' not in raw; put(p,raw+note.encode())
assert all(sha(p)==h for p,h in start.items())
validation=dict(preflight,campaign_id=cid,generated_at=now,status='green_round220_closure_no_complete_source_gain',terminal_label=decision['terminal_label'],starting_graph_sha256=start[gp.as_posix()],final_graph_sha256=sha(gp),graph_nodes=401,original_graph_raw_bytes_unchanged=True,proof_draft_raw_bytes_unchanged=True,final_proof_draft_sha256=sha(draft),previous_ledger_prefix_bytes_unchanged=True,legacy_paths_unchanged=True,next_strategy_checkpoint=223,green_round_gates=len(gates))
write(base/'controls/closure_validation.json',validation)
vtext=f'''# Round220 closure validation

GREEN for scoped source and operator evidence only. Complete actual energy,
signed I12 and full quarter remain OPEN. Identity patch validated, applied
in memory, reversed and replayed; all401 graph nodes, graph/draft bytes
and prior ledger prefix unchanged. All10 gates green; all488 prior archive
entries unchanged. Four bounded current-primary theorem audits, isolated
operator derivation, final-hash reviews and scope controls completed.
Zero mathematical experiments. No complete bound or exponent gain.
Checkpoint220 records the forward UNBAL correction. Round221 pending
design; next broad strategy/current-primary-source review223.
Graph SHA256:{sha(gp)}.
Details:{base.as_posix()}/controls/closure_validation.json.
'''
for p in ['state/last_validation.md','state/last_validation_report.md']: put(p,vtext.encode())
assert not validate_graph(load_graph(gp),root=root) and not validate_campaign(read('state/active_campaign.yml'),g,root=root)
assert not subprocess.check_output(['git','diff','--name-only','--','rounds/obligation-main','rounds/web-research-test']).strip()
subprocess.run(['git','diff','--check'],check=True)
hashes={p.relative_to(root).as_posix():sha(p) for p in sorted((root/base).rglob('*')) if p.is_file() and p.name!='artifact_hashes.json' and '__pycache__' not in p.parts}
for p in [Path('strategy/round220_full_goal_arithmetic_source_review.md'),checkpoint]: hashes[p.as_posix()]=sha(p)
write(base/'controls/artifact_hashes.json',hashes)
print(json.dumps({k:validation[k] for k in ['status','graph_nodes','final_graph_sha256','proof_draft_raw_bytes_unchanged','green_round_gates','protected_archive_entries_checked','pointwise_exponent_change']},indent=2))
