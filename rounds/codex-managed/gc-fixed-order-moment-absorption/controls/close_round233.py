"""Conductor-only reviewed create-one-node closure; preserves all prior graph entries."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,copy,sys
sys.path.insert(0,str(Path(__file__).resolve().parents[4]))
from math_collab.proof_obligations import load_graph,dump_graph,write_graph,validate_graph,validate_patch_against_graph,apply_state_patch,patch_result_summary
from math_collab.campaigns import validate_campaign
root=Path.cwd(); rel=Path('rounds/codex-managed/gc-fixed-order-moment-absorption'); base=root/rel
def read(p): return json.loads(Path(p).read_text(encoding='utf-8'))
def write(p,v): Path(p).write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def prepend(p,s):
 p=Path(p); p.write_bytes(s.encode('utf-8')+b'\n\n---\n\n## Historical record retained below\n\n'+p.read_bytes())
decision=read(base/'closure_decision.json'); assert decision['conductor_review_complete'] and decision['promote_reduction_only']
assert decision['result']=='fixed_order_absorption_reduction_reviewed'
for p,h in decision['reviewed_artifact_hashes'].items(): assert sha(root/p)==h,(p,'changed since review')
for p,h in read(base/'controls/frozen_initial_reports.json').items(): assert sha(root/p)==h,(p,'initial changed')
manifest=read(root/'state/active_campaign.yml'); assert manifest['round_index']==233 and manifest['status']=='review'
plan=read(base/'plan.json')
for key in ['frozen_target','resource_policy','completion_criteria','target_obligations','controls','review_seams']:
 assert manifest[key]==plan['campaign'][key],key
baseline=read(base/'controls/starting_hashes.json')
allowed=plan['artifact_policy']['allowed_workflow_changes']
conditional=plan['artifact_policy']['conditional_promotion_files']
protected=[p for p in baseline if p not in allowed+conditional]
assert all((root/p).is_file() and sha(root/p)==baseline[p] for p in protected)
gp=root/'state/proof_obligations.yml'; dp=root/'state/best_proof_draft.md'
oldraw=gp.read_bytes(); olddraft=dp.read_bytes()
assert sha(gp)==baseline['state/proof_obligations.yml']==manifest['starting_graph_sha256']
assert sha(dp)==baseline['state/best_proof_draft.md']
graph=load_graph(gp); assert len(graph['proof_obligations'])==401 and not validate_graph(graph,root=root)
kernel=root/decision['kernel_path']; candidate=root/decision['candidate_path']
assert sha(candidate)==decision['candidate_sha256']
if kernel.exists(): assert kernel.read_bytes()==candidate.read_bytes()
else: kernel.write_bytes(candidate.read_bytes())
assert sha(kernel)==decision['candidate_sha256']
patch=read(base/'state_patch.json'); assert not validate_patch_against_graph(graph,patch)
node_id=decision['new_node_id']; assert len(patch['proof_obligations']['create'])==1
assert patch['proof_obligations']['create'][0]['id']==node_id
assert all(not patch['proof_obligations'][k] for k in ['update','correct_rejected','reject'])
applied,result=apply_state_patch(graph,patch,round_index=233,judge_ref=(rel/'synthesis.md').as_posix())
assert not validate_graph(applied,root=root)
assert applied['proof_obligations'][:-1]==graph['proof_obligations']
assert all(applied[k]==graph[k] for k in graph if k!='proof_obligations')
idx={n['id']:n for n in applied['proof_obligations']}; done=set()
def walk(n,active):
 assert n in idx and n not in active
 if n in done:return
 assert idx[n]['status'] in ['proved_internal','proved_external_dependency'],(n,idx[n]['status'])
 active.add(n)
 for d in idx[n].get('dependencies',[]):walk(d,active)
 active.remove(n);done.add(n)
walk(node_id,set())
restored=copy.deepcopy(applied); restored['proof_obligations']=[n for n in restored['proof_obligations'] if n['id']!=node_id]
assert restored==graph
assert read(base/'controls/prelaunch_state/proof_obligations.yml')==restored
assert (base/'controls/prelaunch_state/proof_obligations.yml').read_bytes()==oldraw
replay,_=apply_state_patch(restored,patch,round_index=233,judge_ref=(rel/'synthesis.md').as_posix())
replay['proof_obligations'][-1]['last_updated_at']=applied['proof_obligations'][-1]['last_updated_at']
assert replay==applied
for p in idx[node_id]['evidence']['positive']:assert (root/p).is_file(),p
gates=decision['gates']; assert gates and all(g['id'].startswith('round233_') and g['status'].startswith('green') for g in gates)
for g in gates: assert (root/g['artifact']).is_file()
matrix=read(root/'state/validation_matrix.yml'); oldgates=copy.deepcopy(matrix['gates']); assert not any(g['id'].startswith('round233_') for g in oldgates)
now=datetime.now(timezone.utc).isoformat()
preflight={'status':'passed','round_index':233,'starting_graph_sha256':sha(gp),'old_nodes_unchanged':401,'new_node':node_id,'dependency_cone_all_accepted':sorted(done),'inverse_semantic_identity':True,'inverse_original_bytes_snapshot_verified':True,'replay_except_new_timestamp':True,'candidate_kernel_identical':True,'reviewed_artifact_hashes':decision['reviewed_artifact_hashes'],'green_gates':len(gates),'complete_moment_gain':False,'pointwise_gain':False}
write(base/'controls/promotion_preflight.json',preflight)
matrix['gates'].extend(gates); matrix.update(campaign_id=manifest['campaign_id'],promotion_status='round233_green_reduction_only_preflight')
write(root/'state/validation_matrix.yml',matrix)
# First mathematical-state mutation, after all proof and mechanical gates.
assert gp.read_bytes()==oldraw and dp.read_bytes()==olddraft
write_graph(gp,applied); assert load_graph(gp)==applied
gh=sha(gp); matrix.update(graph_sha256=gh,promotion_status='round233_accepted_fixed_order_reduction_only');write(root/'state/validation_matrix.yml',matrix)
dp.write_bytes(olddraft+('\n\n'+decision['draft_addition']+'\n').encode('utf-8'))
assert dp.read_bytes().startswith(olddraft)
manifest.update(status='complete',completed_at=now,terminal_label=decision['result'],closing_assessment=decision['reason'],state_patch=(rel/'state_patch.json').as_posix(),synthesis=(rel/'synthesis.md').as_posix(),resulting_graph_sha256=gh,new_accepted_nodes=[node_id],next_round_automatic=False)
for t in manifest['tasks']:t['status']='complete'
manifest['conductor_interventions'].extend(decision['interventions'])
assert not validate_campaign(manifest,applied,root=root)
ledger=read(root/'state/round_ledger.yml'); previous=read(base/'controls/prelaunch_state/round_ledger.yml')
assert [r for r in ledger['rounds'] if r['round_index']<233]==previous['rounds']
entry=next(r for r in ledger['rounds'] if r['round_index']==233)
entry.update(status='complete',completed_at=now,terminal_label=decision['result'],synthesis=(rel/'synthesis.md').as_posix(),state_patch=(rel/'state_patch.json').as_posix(),assessment=decision['assessment'],resulting_graph_sha256=gh,next_round=234,next_round_status='pending_design_no_automatic_launch')
for t in entry['tasks']:t['status']='complete'
ledger['active_round']=233;write(root/'state/round_ledger.yml',ledger);write(root/'state/active_campaign.yml',manifest)
future=read(root/'state/next_round_plan.yml')
future.update(round_index=234,status='pending_design',campaign_id=None,tasks=[],predecessor_round=233,predecessor_terminal_label=decision['result'],candidate_objective=decision['future_constraint'],latest_completed_campaign=manifest['campaign_id'],next_round_automatic=False,resulting_graph_sha256=gh)
future['round233_closure']={'completed_at':now,'synthesis':(rel/'synthesis.md').as_posix(),'new_node':node_id,'first_gap':'Actual signed distinct-class integral upper bounds, with sublinear exponent along unbounded fixed even orders for quarter.','complete_moment_gain':False,'pointwise_gain':False}
future['quantitative_gates']['quarter_moment_route']='Accepted233 fixed-order absorption now supplies complete signed distinct-class equivalence above paid head/error budgets; a family b_p=o(p) of actual signed estimates is still OPEN. Choose p before T.'
write(root/'state/next_round_plan.yml',future)
for name in ['state/current_round.md','state/next_campaign.md']:(root/name).write_text(decision['status_summary']+'\n',encoding='utf-8')
for name in ['state/project_summary.md','state/current_state.md','manifests/reading_packet.md']:prepend(root/name,decision['status_summary'])
prepend(root/'state/failure_ledger.md',decision['barrier_summary'])
assert all(sha(root/p)==baseline[p] for p in protected)
assert [r for r in read(root/'state/round_ledger.yml')['rounds'] if r['round_index']<233]==previous['rounds']
assert read(root/'state/validation_matrix.yml')['gates'][:-len(gates)]==oldgates==read(base/'controls/prelaunch_state/validation_matrix.yml')['gates']
assert load_graph(gp)['proof_obligations'][:-1]==graph['proof_obligations']
assert not validate_graph(load_graph(gp),root=root) and not validate_campaign(read(root/'state/active_campaign.yml'),applied,root=root)
record={'status':'passed','round_index':233,'completed_at':now,'terminal_label':decision['result'],'graph_nodes':402,'prior_nodes_unchanged':401,'new_node':node_id,'starting_graph_sha256':baseline['state/proof_obligations.yml'],'resulting_graph_sha256':gh,'patch_summary':patch_result_summary(result),'protected_preexisting_files_checked':len(protected),'prior_ledger_entries_unchanged':True,'prior_validation_gates_unchanged':True,'proof_draft_old_bytes_preserved':True,'initial_reports_unchanged':True,'inverse_semantic_identity':True,'inverse_original_bytes_snapshot_verified':True,'replay_except_new_timestamp':True,'green_gates':len(gates),'complete_moment_gain':False,'pointwise_gain':False,'next_round':'234 pending_design, no tasks, no launch'}
write(base/'controls/closure_validation.json',record)
vt='# Round233 validation passed\n\n'+decision['reason']+'\n\nOne reduction node added; all401 old nodes unchanged. Proof draft appended only after graph promotion, with old bytes retained. Final-hash reviews, Wolfram/local controls, accepted dependency cone, reverse/replay, prior ledger/matrix and protected-history checks passed. No complete moment or pointwise improvement. Details: '+(rel/'controls/closure_validation.json').as_posix()+'.\n'
for name in ['state/last_validation.md','state/last_validation_report.md']:(root/name).write_text(vt,encoding='utf-8')
artifacts={p.relative_to(root).as_posix():sha(p) for p in base.rglob('*') if p.is_file() and 'prelaunch_state' not in p.parts and p.name!='final_artifact_hashes.json' and p.suffix!='.pyc'}
artifacts[kernel.relative_to(root).as_posix()]=sha(kernel);write(base/'controls/final_artifact_hashes.json',artifacts)
print(json.dumps(record))
