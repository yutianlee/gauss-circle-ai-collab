"""Validate the complete analytic attempt and close it with an identity patch."""
import copy, hashlib, json, re, subprocess, sys
from pathlib import Path
from datetime import datetime, timezone
root=Path.cwd();sys.path.insert(0,str(root))
from math_collab.campaigns import validate_campaign, _next_campaign
from math_collab.proof_obligations import load_graph, dump_graph, validate_graph, validate_patch_against_graph, apply_state_patch

cid='gc-complete-signed-convolution-attack';base=Path('rounds/codex-managed')/cid
terminal='complete_analytic_attempt_no_new_bound'
now=datetime.now(timezone.utc).isoformat()
def read(p):return json.loads(Path(p).read_text(encoding='utf-8'))
def write(p,o):Path(p).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
start=read(base/'controls/starting_state_hashes.json')
assert all(sha(p)==h for p,h in start.items()),'Protected starting state changed'
for p,h in read(base/'controls/frozen_artifact_hashes.json').items():assert sha(p)==h,('Frozen input changed',p)
for prior in ['m9-m1-t1-complete-source-coefficient-mask-analysis','gc-whole-discrepancy-twelfth-moment','gc-strategy-signed-moment-majorant-review']:
 for p,h in read(Path('rounds/codex-managed')/prior/'controls/artifact_hashes.json').items():assert sha(p)==h,('Closed artifact changed',p)
gp=Path('state/proof_obligations.yml');oldraw=gp.read_bytes();g=load_graph(gp)
assert len(g['proof_obligations'])==398 and not validate_graph(g,root=root)
m=read('state/active_campaign.yml')
assert m['round_index']==203 and m['campaign_id']==cid and m['status']=='active'
assert not validate_campaign(m,g,root=root)
frozen=read(base/'plan.json')['campaign']
for key in ['frozen_target','completion_criteria','resource_policy','controls','target_obligations','review_seams']:
 assert m[key]==frozen[key],('Frozen scope drift',key)
for t,f in zip(m['tasks'],frozen['tasks']):
 assert {k:v for k,v in t.items() if k!='status'}=={k:v for k,v in f.items() if k!='status'}
 s=Path(t['report_path']).read_text(encoding='utf-8')
 assert all(re.search(rf'^## {i}\.',s,re.M) for i in range(1,8)),t['id']
reviews=[
 (base/'reviews/independent_density_remainder_review.md',base/'reports/actual_density_remainder_attack.md'),
 (base/'reviews/independent_arithmetic_packet_review.md',base/'reports/arithmetic_signed_tail_attack.md'),
 (base/'reviews/independent_radial_poisson_review.md',base/'controls/conductor_radial_poisson_analysis.md')]
for review,artifact in reviews:
 s=review.read_text(encoding='utf-8')
 scoped_pass=('PASS for the stated complete radial block identity' in s) if review.name=='independent_radial_poisson_review.md' else ('GREEN' in s)
 assert scoped_pass and sha(artifact).lower() in s.lower(),('Scoped verdict or exact hash absent',review)
 assert all(re.search(rf'^## {i}\.',s,re.M) for i in range(1,8)),review
judge=base/'reviews/conductor_round203_reconciliation.md'
assert 'GREEN for bounded analytic closure only' in judge.read_text(encoding='utf-8')
assert (base/'synthesis.md').is_file()
hygiene=[]
for p in base.rglob('*.md'):
 s=p.read_text(encoding='utf-8')
 assert '\ufffd' not in s and not any(ord(c)<32 and c not in '\n\r\t' for c in s),p
 hygiene.append(p.as_posix())
protected=['GC-target','Conditional-bridge','M9','M9-M1','M9-M2','M9-endpoint-uniformity','GC-external-Li-Yang-theta-star','GC-weighted-square-root-exact-resonance-mass','GC-physical-twelfth-moment-absolute-majorant-obstruction']
patch=dict(round_index=203,campaign_id=cid,starting_graph_sha256=start[gp.as_posix()],
 proof_obligations=dict(create=[],update=[],correct_rejected=[],reject=[],no_change=protected),
 round_assessment=dict(terminal_label=terminal,reason='Complete density and arithmetic attempts include all tails and errors, but establish no new complete moment bound. The strongest inherited norm exponent remains0.648072478; target0.58 and all parent/exponent claims remain open.'),
 reversibility=dict(rule='Identity patch; in-memory application, reversal and replay equal the entire original graph. Preserve original graph and proof-draft bytes without serialization.'))
assert not validate_patch_against_graph(g,patch)
applied,result=apply_state_patch(copy.deepcopy(g),patch,round_index=203,judge_ref=judge.as_posix())
assert applied==g and not result.created and not result.updated and not result.rejected and not result.corrected_rejected
replay,_=apply_state_patch(copy.deepcopy(applied),patch,round_index=203,judge_ref=judge.as_posix())
assert replay==g and dump_graph(replay)==dump_graph(g)
write(base/'state_patch.json',patch)
preflight=dict(round_index=203,status='green_identity_patch_preflight',graph_schema='pass',campaign_schema='pass',identity_patch='pass',
 all_398_nodes_and_all_other_graph_data_unchanged=True,reverse_identity_replay='pass',
 exact_review_hashes={a.as_posix():sha(a) for _,a in reviews},
 frozen_scope_and_briefs_unchanged=True,closed_round200_201_202_archives_unchanged=True,
 report_hygiene=hygiene,mathematical_numerical_experiments=0,analytic_target='open',exponent_change=False)
write(base/'controls/closure_preflight.json',preflight)
matrix=read('state/validation_matrix.yml')
for gate in matrix['gates']:
 if gate['id'].startswith('round203_'):gate['status']='green_bounded_attempt_only_target_open'
for review,_ in reviews:
 matrix['gates'].append(dict(id='round203_'+review.stem,status='green',artifact=review.as_posix()))
matrix['gates'].append(dict(id='round203_identity_patch_scope',status='green',artifact=(base/'controls/closure_preflight.json').as_posix()))
assert all(x['status'].startswith('green') and Path(x['artifact']).is_file() for x in matrix['gates'] if x['id'].startswith('round203_'))
matrix.update(promotion_status='round_203_closed_identity_patch_no_new_bound',graph_sha256=sha(gp),
 analytic_target_status='open_complete_signed_filtered_convolution',
 decision_rule='Round203 closes a bounded complete analytic attempt with no new norm bound. Identity State Patch; every accepted node and exponent unchanged. Round204 remains pending design; broad review205.')
write('state/validation_matrix.yml',matrix)
# The validated State Patch is the identity: deliberately do not rewrite graph or draft.
assert gp.read_bytes()==oldraw and all(sha(p)==h for p,h in start.items())
assessment=dict(decision='retain_open_target_archive_complete_analytic_attempt',terminal_label=terminal,graph_mutation=False,
 main_result=patch['round_assessment']['reason'],resulting_graph_sha256=sha(gp),
 patch_effect=f'0_create_0_update_0_correct_0_reject_{len(protected)}_no_change',exponent_change=False)
m.update(status='complete',completed_at=now,closing_assessment=assessment,post_report_reviews=[p.as_posix() for p,_ in reviews])
for t in m['tasks']:t['status']='completed'
assert not validate_campaign(m,g,root=root);write('state/active_campaign.yml',m)
lp=Path('state/round_ledger.yml');s=lp.read_text(encoding='utf-8');ledger=json.loads(s)
assert ledger['active_round']==203 and ledger['rounds'][-1]['round_index']==203
entry=ledger['rounds'][-1];entry.update(status='closed',closing_assessment=assessment,completed_at=now,next_round=204)
for t in entry['tasks']:t['status']='completed'
pos=s.rfind('    {\n      "round_index": 203,');assert pos>0
new=s[:pos]+'\n'.join('    '+line for line in json.dumps(entry,indent=2,ensure_ascii=False).splitlines())+'\n  ]\n}\n'
assert json.loads(new)==ledger;lp.write_text(new,encoding='utf-8')
# The round is now closed. Record a prospective direction, not a frozen successor.
write('state/next_round_plan.yml',dict(round_index=204,status='pending_design',campaign_id=None,starting_graph_sha256=sha(gp),predecessor_round=203,predecessor_terminal_label=terminal,tasks=[],
 candidate_objective='Attempt a quantitative large-value distribution estimate for the complete actual tail on the radius window, using its correlated arithmetic packets. Target weighted measure{|B|>V} << T^(29/25+epsilon)V^(-12) for T^(54/775)<=V<=T^(beta+epsilon); low values are covered by the inherited q0 moment. Prove a saving, not just the layer-cake equivalence.',
 design_constraint='Do not repeat generic smoothing or area-density subtraction: their complete pure remainders retain the target. Audit an actual large-values argument, preserve coefficient phases and all ranges, and compare to the0.068072478 norm gap. Select and freeze tasks only after inspecting closed203 artifacts.',
 full_goal_scope='Target implies only102/325 if proved; quarter theorem and all internal frontiers remain open.',
 scheduled_review='Mandatory broad strategy/current-literature review205 after202--204.'))
summary=_next_campaign(m,output_dir=base,graph_hash=sha(gp))
summary+='\n## Closing decision\n\nNo new complete norm bound. Density and arithmetic remainders were fully priced; generic smoothing cannot discard the pure remainder. Identity State Patch; graph and proof draft unchanged. Round204 is pending design, broad review205.\n'
for p in ['state/current_round.md','state/next_campaign.md']:Path(p).write_text(summary,encoding='utf-8')
note='''
## Round 203 complete analytic attempt (2026-09-23)

The actual continuous density and all mixed density/remainder factors
are subtarget, but the pure arithmetic remainder retains the complete
moment difficulty. Independent divisor-Poisson and radial-Poisson
estimates return the classical scale. The strongest inherited norm
bound remains T^(0.648072478+epsilon), leaving0.068072478 to the
target exponent0.58. Generic smoothing transfers the full norm into
one of its two pieces; it supplies no arithmetic gain.

Round203 closed with a validated identity State Patch. All398 graph
nodes, the proof draft and every accepted exponent are unchanged.
No new external theorem or numerical evidence was imported. See
`rounds/codex-managed/gc-complete-signed-convolution-attack/synthesis.md`.
Round204 is pending design; the mandatory broad review remains205.
'''
for p in ['state/project_summary.md','state/current_state.md']:
 q=Path(p);old=q.read_text(encoding='utf-8');assert '## Round 203 complete analytic attempt' not in old
 q.write_text(old.rstrip()+'\n'+note,encoding='utf-8')
assert not subprocess.check_output(['git','diff','--name-only','--','rounds/obligation-main','rounds/web-research-test']).strip()
assert all(sha(p)==h for p,h in start.items())
validation=dict(preflight,status='green_round203_closure_no_new_bound',campaign_id=cid,generated_at=now,
 terminal_label=terminal,starting_graph_sha256=start[gp.as_posix()],final_graph_sha256=sha(gp),
 canonical_graph_sha256=hashlib.sha256(dump_graph(g).encode()).hexdigest(),graph_nodes=398,
 original_graph_raw_bytes_unchanged=True,proof_draft_raw_bytes_unchanged=True,
 all_previous_ledger_entries_unchanged=True,legacy_paths_unchanged=True,next_strategy_checkpoint=205)
write(base/'controls/closure_validation.json',validation)
text=(f'# Round203 closure validation\n\nGREEN for complete bounded analytic closure; actual signed norm target OPEN.\n\n'
 f'Graph SHA256: `{sha(gp)}`. The identity State Patch was validated, applied in memory, reversed and replayed with exact equality. '
 'All398 nodes, all other graph data, and original graph/proof-draft bytes remain unchanged. '
 'Three seven-section reports, three exact-hash seam reviews, conductor reconciliation, frozen-scope checks, '
 'protected Round200--202 archive hashes and file hygiene passed. No new exponent or theorem is promoted.\n\n'
 'Graph-schema validation does not reprove historical nodes or erase inherited legacy advisories. '
 'No mathematical numerical experiment was performed. Round204 is pending design; broad strategy/literature review205 remains mandatory.\n\n'
 f'Details: `{base.as_posix()}/controls/closure_validation.json`.\n')
for p in ['state/last_validation.md','state/last_validation_report.md']:Path(p).write_text(text,encoding='utf-8')
assert not validate_graph(load_graph(gp),root=root) and not validate_campaign(read('state/active_campaign.yml'),g,root=root)
subprocess.run(['git','diff','--check'],check=True)
hashes={p.relative_to(root).as_posix():sha(p) for p in sorted((root/base).rglob('*')) if p.is_file() and p.name!='artifact_hashes.json' and '__pycache__' not in p.parts}
strategy=Path('strategy/round203_complete_signed_convolution_attack.md');hashes[strategy.as_posix()]=sha(strategy)
write(base/'controls/artifact_hashes.json',hashes)
print(json.dumps({k:validation[k] for k in ['status','graph_nodes','final_graph_sha256','proof_draft_raw_bytes_unchanged','exponent_change']},indent=2))
