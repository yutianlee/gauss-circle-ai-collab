"""Conductor-only identity closure. Requires completed, reviewed decision artifacts."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys
sys.path.insert(0,str(Path(__file__).resolve().parents[4]))
from math_collab.proof_obligations import load_graph,validate_graph,validate_patch_against_graph,apply_state_patch,patch_result_summary
from math_collab.campaigns import validate_campaign

root=Path.cwd()
rel=Path('rounds/codex-managed/gc-connected-cumulant-test')
base=root/rel
def read(p): return json.loads(Path(p).read_text(encoding='utf-8'))
def write(p,v): Path(p).write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def prepend(p,text):
    p=Path(p)
    p.write_bytes(text.encode('utf-8')+b'\n\n---\n\n## Historical record retained below\n\n'+p.read_bytes())

decision=read(base/'closure_decision.json')
assert decision['conductor_review_complete'] is True
assert decision['result']=='connected_correlation_test_closed_without_complete_gain'
for name,expected in decision['reviewed_artifact_hashes'].items():
    assert sha(root/name)==expected,(name,'changed since review')
for name,expected in read(base/'controls/frozen_initial_reports.json').items():
    assert sha(root/name)==expected,(name,'initial report changed')
assert (base/'synthesis.md').is_file()
manifest=read(root/'state/active_campaign.yml')
assert manifest['campaign_id']=='gc-connected-cumulant-test' and manifest['status']=='review'
graph=load_graph(root/'state/proof_obligations.yml')
assert not validate_graph(graph,root=root)
graph_hash=sha(root/'state/proof_obligations.yml')
assert graph_hash==manifest['starting_graph_sha256']
baseline=read(base/'controls/starting_hashes.json')
allowed=read(base/'plan.json')['artifact_policy']['allowed_workflow_changes']
protected=[name for name in baseline if name not in allowed]
assert all((root/name).is_file() and sha(root/name)==baseline[name] for name in protected)
assert len(graph['proof_obligations'])==402
now=datetime.now(timezone.utc).isoformat()

patch={
    'round_index':234,'campaign_id':manifest['campaign_id'],'starting_graph_sha256':graph_hash,
    'proof_obligations':{'create':[],'update':[],'correct_rejected':[],'reject':[],
        'no_change':['GC-target','Conditional-bridge','M9','M9-M1','M9-M2','M9-endpoint-uniformity',
          'M9-M1-global-angular-radial-estimate','M9-M1-global-lower-radial-signed-estimate',
          'M9-M1-GAR-total-active-equivalence','GC-external-Li-Yang-theta-star',
          'GC-complete-square-root-large-values-moment-bound','GC-complete-distinct-radical-twelfth-reduction','GC-complete-fixed-even-moment-distinct-absorption']},
    'round_assessment':{'terminal_label':decision['result'],'reason':decision['reason']},
    'reversibility':{'rule':'Identity in-memory application, inverse and replay; graph and proof-draft bytes are never rewritten.'}}
write(base/'state_patch.json',patch)
assert not validate_patch_against_graph(graph,patch)

matrix=read(root/'state/validation_matrix.yml')
new_gates=decision['gates']
assert new_gates and all(g['id'].startswith('round234_') and g['status'].startswith('green') for g in new_gates)
for gate in new_gates:
    assert (root/gate['artifact']).is_file(),gate
existing_new=[g for g in matrix['gates'] if g['id'].startswith('round234_')]
assert not existing_new or existing_new==new_gates
matrix.update(campaign_id=manifest['campaign_id'],promotion_status='round234_identity_closure_connected_test',graph_sha256=graph_hash)
if not existing_new: matrix['gates'].extend(new_gates)
write(root/'state/validation_matrix.yml',matrix)

# Apply only after the reviewed closure gates are green. Identity application stays in memory.
applied,result=apply_state_patch(graph,patch,round_index=234,judge_ref=(rel/'synthesis.md').as_posix())
assert not validate_graph(applied,root=root)
assert applied==graph
inverse,_=apply_state_patch(applied,patch,round_index=234)
replayed,_=apply_state_patch(inverse,patch,round_index=234)
assert inverse==graph and replayed==applied

manifest.update(status='complete',completed_at=now,terminal_label=decision['result'],
    closing_assessment=decision['reason'],state_patch=(rel/'state_patch.json').as_posix(),
    synthesis=(rel/'synthesis.md').as_posix(),attempts_on_current_premise_completed=1,
    next_round_automatic=False,mandatory_strategy_reassessment_complete=True,resulting_graph_sha256=graph_hash,attempts_on_connected_premise_completed=1)
for task in manifest['tasks']: task['status']='complete'
manifest['conductor_interventions'].extend(decision['interventions'])
assert not validate_campaign(manifest,graph,root=root)

ledger=read(root/'state/round_ledger.yml')
previous=read(base/'controls/prelaunch_state/round_ledger.yml')
assert [r for r in ledger['rounds'] if r['round_index']<234]==previous['rounds']
entry=next(r for r in ledger['rounds'] if r['round_index']==234)
entry.update(status='complete',completed_at=now,terminal_label=decision['result'],
    synthesis=(rel/'synthesis.md').as_posix(),state_patch=(rel/'state_patch.json').as_posix(),
    assessment=decision['assessment'],next_round=235,next_round_status='pending_design_no_automatic_launch')
for task in entry['tasks']: task['status']='complete'
ledger['active_round']=234  # Last numbered campaign remains the current completed record.
write(root/'state/round_ledger.yml',ledger)
write(root/'state/active_campaign.yml',manifest)

future=read(root/'state/next_round_plan.yml')
future.update(round_index=235,status='pending_design',campaign_id=None,tasks=[],predecessor_round=234,
    predecessor_terminal_label=decision['result'],candidate_objective=decision['future_constraint'],
    latest_completed_campaign=manifest['campaign_id'],attempts_on_current_premise_completed=1,prior_upper_tail_attempts_completed=2,attempts_on_connected_premise_completed=1,
    next_round_automatic=False,mandatory_strategy_reassessment_complete=True,
    strategy_reassessment='rounds/codex-managed/gc-upper-tail-separated-products/candidates/strategy_reassessment.md',starting_graph_sha256=graph_hash,resulting_graph_sha256=graph_hash)
future['round234_closure']={'completed_at':now,'synthesis':(rel/'synthesis.md').as_posix(),
    'first_gap':'Actual one-sided signed connected12 sum at29/25; disconnected contribution is paid but connected tuplewise absolute mass is at least T^(5/2).' ,
    'graph_effect':'Identity State Patch; no graph or proof-draft change.',
    'attempt_count_on_connected_premise':1,'result':decision['result']}
write(root/'state/next_round_plan.yml',future)

summary=decision['status_summary']
for name in ['state/current_round.md','state/next_campaign.md']:
    (root/name).write_text(summary+'\n',encoding='utf-8')
for name in ['state/project_summary.md','state/current_state.md','manifests/reading_packet.md']:
    prepend(root/name,summary)
prepend(root/'state/failure_ledger.md',decision['barrier_summary'])

assert all(sha(root/name)==baseline[name] for name in protected)
assert sha(root/'state/best_proof_draft.md')==baseline['state/best_proof_draft.md']
assert sha(root/'state/proof_obligations.yml')==graph_hash
assert [r for r in read(root/'state/round_ledger.yml')['rounds'] if r['round_index']<234]==previous['rounds']
assert read(root/'state/validation_matrix.yml')['gates'][:-len(new_gates)]==read(base/'controls/prelaunch_state/validation_matrix.yml')['gates']
assert not validate_graph(load_graph(root/'state/proof_obligations.yml'),root=root)
assert not validate_campaign(read(root/'state/active_campaign.yml'),graph,root=root)
result_record={
    'status':'passed','completed_at':now,'round_index':234,'terminal_label':decision['result'],
    'graph_sha256':graph_hash,'graph_nodes':402,'proof_draft_unchanged':True,
    'identity_application':True,'inverse_identity':True,'replay_identity':True,
    'patch_summary':patch_result_summary(result),'protected_preexisting_files_checked':len(protected),
    'prior_ledger_entries_unchanged':True,'prior_validation_gates_unchanged':True,
    'initial_reports_unchanged':True,'reviewed_artifact_hashes':decision['reviewed_artifact_hashes'],
    'new_gates':new_gates,'next_round':'235 pending_design, no tasks, no launch'}
write(base/'controls/closure_validation.json',result_record)
validation_text='# Round234 validation passed\n\n'+decision['reason']+'\n\n402-node graph and proof draft unchanged. All three initial reports frozen; statement-only derivation and nonauthor final-hash reviews complete; full-harmonic controls and exact Wolfram/local checks passed. No new complete signed estimate. Identity State Patch validated, applied in memory, inverted and replayed. Historical protected files and prior ledger/matrix entries preserved. Full details: '+(rel/'controls/closure_validation.json').as_posix()+'.\n'
for name in ['state/last_validation.md','state/last_validation_report.md']:
    (root/name).write_text(validation_text,encoding='utf-8')
artifacts={p.relative_to(root).as_posix():sha(p) for p in base.rglob('*') if p.is_file() and 'prelaunch_state' not in p.parts and p.name!='final_artifact_hashes.json' and p.suffix!='.pyc'}
write(base/'controls/final_artifact_hashes.json',artifacts)
print(json.dumps({k:result_record[k] for k in ['status','round_index','graph_nodes','terminal_label','protected_preexisting_files_checked','next_round']}))
