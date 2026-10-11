"""Close the reviewed208 strategy campaign with an identity State Patch."""
import copy,hashlib,json,re,subprocess,sys,time
from datetime import datetime,timezone
from pathlib import Path
root=Path.cwd();sys.path.insert(0,str(root))
from math_collab.campaigns import validate_campaign,_next_campaign
from math_collab.proof_obligations import load_graph,dump_graph,validate_graph,validate_patch_against_graph,apply_state_patch
cid='gc-full-proof-signed-arithmetic-review';base=Path('rounds/codex-managed')/cid
gp=Path('state/proof_obligations.yml');now=datetime.now(timezone.utc).isoformat()
checkpoint=Path('strategy/gauss_circle_strategy_checkpoint_round208_2026-09-27.md')
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def put(p,b):
 for attempt in range(5):
  try:Path(p).write_bytes(b);return
  except OSError:
   if attempt==4:raise
   time.sleep(.2)
def write(p,o):put(p,(json.dumps(o,indent=2,ensure_ascii=False)+'\n').encode('utf-8'))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def contract(p):
 s=Path(p).read_text(encoding='utf-8');assert all(re.search(rf'^#{{1,2}} {i}\.',s,re.M) for i in range(1,8)),p;return s
start=read(base/'controls/starting_state_hashes.json')
assert all(sha(p)==h for p,h in start.items())
for p,h in read(base/'controls/frozen_artifact_hashes.json').items():assert sha(p)==h,('frozen',p)
priors=['m9-m1-t1-complete-source-coefficient-mask-analysis','gc-whole-discrepancy-twelfth-moment',
'gc-strategy-signed-moment-majorant-review','gc-complete-signed-convolution-attack','gc-complete-large-values-duality',
'gc-full-frontier-moment-strategy-review','gc-complete-signed-shell-arithmetic','gc-signed-rational-filter-attack']
archive_count=0
for prior in priors:
 for p,h in read(Path('rounds/codex-managed')/prior/'controls/artifact_hashes.json').items():assert sha(p)==h,('archive',p);archive_count+=1
raw_graph=gp.read_bytes();g=load_graph(gp);assert len(g['proof_obligations'])==399 and not validate_graph(g,root=root)
m=read('state/active_campaign.yml');assert m['round_index']==208 and m['campaign_id']==cid and m['status']=='active'
assert not validate_campaign(m,g,root=root)
frozen=read(base/'plan.json')['campaign']
for key in ['frozen_target','completion_criteria','resource_policy','controls','target_obligations','review_seams']:assert m[key]==frozen[key],key
for t,f in zip(m['tasks'],frozen['tasks']):
 assert {k:v for k,v in t.items() if k!='status'}=={k:v for k,v in f.items() if k!='status'}
 contract(t['report_path'])
assert len(m['tasks'])==len(frozen['tasks'])==3
power=base/'controls/conductor_bandlimited_strategy.md';contract(power)
reviews=[
 (base/'reviews/independent_bandlimited_peak_review.md',[power]),
 (base/'reviews/independent_hierarchy_gate_review.md',[base/'reports/blind_moment_hierarchy.md',power]),
 (base/'reviews/independent_harmonic_source_review.md',[base/'reports/harmonic_current_sources.md',power]),
 (base/'reviews/conductor_arithmetic_source_review.md',[base/'reports/arithmetic_full_frontier.md'])]
for p,arts in reviews:
 s=contract(p);assert 'GREEN' in s,p
 for a in arts:assert sha(a) in s.lower(),('review binding',p,a)
assert checkpoint.is_file() and (base/'synthesis.md').is_file()
evidence=[Path(t['report_path']) for t in m['tasks']]+[power]+[p for p,_ in reviews]+[checkpoint]
judge=base/'reviews/conductor_round208_reconciliation.md';s=judge.read_text(encoding='utf-8')
assert 'FINAL_HASH_BINDINGS' in s
bindings='\n'.join(f'- `{p.as_posix()}`: `{sha(p)}`.' for p in evidence)
put(judge,s.replace('FINAL_HASH_BINDINGS',bindings).encode('utf-8'));assert 'GREEN for strategy-review closure only' in contract(judge)
hygiene=[]
for p in list(base.rglob('*.md'))+[checkpoint]:
 raw=p.read_bytes();s=raw.decode('utf-8');assert not re.search(rb'\r(?!\n)',raw),p
 assert '\ufffd' not in s and not any(ord(c)<32 and c not in '\n\r\t' for c in s),p
 hygiene.append(p.as_posix())
protected=['GC-target','Conditional-bridge','M9','M9-M1','M9-M2','M9-endpoint-uniformity','GC-external-Li-Yang-theta-star',
'GC-weighted-square-root-exact-resonance-mass','GC-physical-twelfth-moment-absolute-majorant-obstruction','GC-complete-square-root-large-values-moment-bound']
reason=('Current sources supply no arithmetic gain. A reviewed local Fourier reproduction bridge selects the complete '
'tenth-moment gate K10(N)<<T^(473/65+epsilon)N^-1/2 on T^(166/325)<N<T^(242/325), with all complements paid. '
'Its conditional pointwise consequence is102/325; the actual gate and full quarter theorem remain open.')
patch=dict(round_index=208,campaign_id=cid,starting_graph_sha256=start[gp.as_posix()],
proof_obligations=dict(create=[],update=[],correct_rejected=[],reject=[],no_change=protected),
round_assessment=dict(terminal_label='costed_strategy_adjustment',reason=reason),
reversibility=dict(rule='Identity in-memory application, inverse and replay; graph/draft bytes never rewritten.'))
assert not validate_patch_against_graph(g,patch)
applied,result=apply_state_patch(copy.deepcopy(g),patch,round_index=208,judge_ref=judge.as_posix())
assert applied==g and not any([result.created,result.updated,result.rejected,result.corrected_rejected])
inverse=copy.deepcopy(applied);replay,_=apply_state_patch(copy.deepcopy(inverse),patch,round_index=208,judge_ref=judge.as_posix())
assert inverse==g and replay==g and dump_graph(replay)==dump_graph(g)
write(base/'state_patch.json',patch)
preflight=dict(round_index=208,status='green_identity_patch_preflight',graph_schema='pass',campaign_schema='pass',
identity_patch='pass',reverse_identity_replay='pass',all_399_nodes_and_other_graph_data_unchanged=True,
exact_review_hashes={a.as_posix():sha(a) for _,arts in reviews for a in arts},
three_report_hashes={t['report_path']:sha(t['report_path']) for t in m['tasks']},
frozen_scope_and_briefs_unchanged=True,closed_round200_through207_archives_unchanged=True,
protected_archive_entries_checked=archive_count,report_hygiene=hygiene,mathematical_numerical_experiments=0,
analytic_target='open',complete_moment_bound_improved=False,pointwise_exponent_change=False,
conditional_bridge_changed_next_action=True)
write(base/'controls/closure_preflight.json',preflight)
matrix=read('state/validation_matrix.yml');oldgates=copy.deepcopy([x for x in matrix['gates'] if not x['id'].startswith('round208_')])
for gate in matrix['gates']:
 if gate['id'].startswith('round208_'):gate['status']='green_strategy_scope_only_arithmetic_target_open'
for review,_ in reviews:matrix['gates'].append(dict(id='round208_'+review.stem,status='green',artifact=review.as_posix()))
matrix['gates'].append(dict(id='round208_identity_patch_scope',status='green',artifact=(base/'controls/closure_preflight.json').as_posix()))
assert all(x['status'].startswith('green') and Path(x['artifact']).is_file() for x in matrix['gates'] if x['id'].startswith('round208_'))
assert oldgates==[x for x in matrix['gates'] if not x['id'].startswith('round208_')]
matrix.update(promotion_status='round_208_closed_identity_patch_costed_strategy',graph_sha256=sha(gp),
analytic_target_status='open_complete_signed_block_tenth_moment',decision_rule='Reviewed strategy/conditional bridge only. Actual K10 and full quarter remain open.209 pending design; next review211.')
write('state/validation_matrix.yml',matrix)
assert gp.read_bytes()==raw_graph and all(sha(p)==h for p,h in start.items())
assessment=dict(decision='retain_graph_adopt_reviewed_conditional_peak_gate',terminal_label='costed_strategy_adjustment',
graph_mutation=False,main_result=reason,resulting_graph_sha256=sha(gp),patch_effect='0_create_0_update_0_correct_0_reject_10_no_change',
complete_moment_bound_improved=False,pointwise_exponent_change=False,
goal_turn_classification='progress_completed_required_source_review_and_new_complete_conditional_bridge_changes_next_action')
m.update(status='complete',completed_at=now,closing_assessment=assessment,post_report_reviews=[p.as_posix() for p,_ in reviews],
conductor_interventions=['Substituted fresh Xiao--Li interface for repeated Matthiesen audit within frozen source budget.',
'Preserved original statement-only isolation, then assigned separate nonblind same-round reviews.',
'Derived local finite-band reproduction and compared complete p6,p8,p10 gates before selection.',
'Retained W^8 in the existing tenth-moment certificate and explicit206 bridge errors.',
'Applied independent H8 correction max(1,E_p), with concrete source application powers unchanged.',
'Distinguished source advice from final conductor selection; all complete complements and full-proof scope retained.',
'Recovered the final initialization manifest write from the frozen plan after transient filesystem error; did not rerun prepare.'])
for t in m['tasks']:t['status']='completed'
assert not validate_campaign(m,g,root=root);write('state/active_campaign.yml',m)
lp=Path('state/round_ledger.yml');ledger_raw=lp.read_bytes();s=ledger_raw.decode('utf-8');ledger=json.loads(s)
assert ledger['active_round']==208 and ledger['rounds'][-1]['round_index']==208
oldentries=copy.deepcopy(ledger['rounds'][:-1]);entry=ledger['rounds'][-1]
entry.update(status='closed',closing_assessment=assessment,completed_at=now,next_round=209)
for t in entry['tasks']:t['status']='completed'
matches=list(re.finditer(r'    \{\r?\n      "round_index": 208,',s));assert len(matches)==1;pos=matches[0].start();eol='\r\n' if '\r\n' in s else '\n'
new=s[:pos]+eol.join('    '+line for line in json.dumps(entry,indent=2,ensure_ascii=False).splitlines())+eol+'  ]'+eol+'}'+eol
assert json.loads(new)==ledger and json.loads(new)['rounds'][:-1]==oldentries
assert new[:pos].encode()==ledger_raw[:len(s[:pos].encode())];put(lp,new.encode())
write('state/next_round_plan.yml',dict(round_index=209,status='pending_design',campaign_id=None,starting_graph_sha256=sha(gp),
predecessor_round=208,predecessor_terminal_label='costed_strategy_adjustment',tasks=[],
candidate_objective='Prove the complete actual signed K10(N)<<T^(473/65+epsilon)N^-1/2 for all dyadic T^(166/325)<N<T^(242/325), or obtain another fully restored pointwise improvement.',
candidate_method='Actual-coefficient phase-sensitive high values, signed shell correlations, or fully paid fifth rational convolution; retain both arms, all near frequencies, masks and width. No identity alone counts as gain.',
first_unproved_estimate='K10 gate(B8); existing T^7N^-3/110+T^(6+8omega) leaves profile8omega-83/65+alpha/2, worst7beta-101/130.',
exact_closed_dependencies=[p.as_posix() for p in evidence]+[judge.as_posix(),(base/'synthesis.md').as_posix()],
design_constraint='Design only from closed208; include the complete band and already proved complements. The old p12 target is not claimed; do not drop W^8 or count another convolution identity as an estimate.',
full_goal_scope='A success here implies only102/325. Full quarter requires b tending to0 with adequate fixed order and explicitly verified expanding bands, or full alternative parents. M1/M2 remain open.',
scheduled_review='Next broad strategy/current-literature review211 after208--210.',prior_turn_classification=assessment['goal_turn_classification']))
summary=_next_campaign(m,output_dir=base,graph_hash=sha(gp))+'\n## Closing decision\n\nRound208 complete: costed strategy adjustment and reviewed conditional local-peak bridge. Identity patch; no arithmetic/exponent gain.209 pending design around the complete tenth-moment gate. Next broad review211.\n'
for p in ['state/current_round.md','state/next_campaign.md']:put(p,summary.encode())
note='''\n## Round208 complete strategy review (2026-09-27)

The reviewed local Fourier reproduction bridge selects K10(N)<<T^(473/65+epsilon)N^-1/2
for EVERY dyadic T^(166/325)<N<T^(242/325), with all complementary frequencies,
explicit shell errors, real endpoints and infinite tails paid. This conditional gate
would imply102/325 directly; it does not claim the earlier complete p12 milestone.
The existing tenth bound retains both T^7N^-3/110 and T^(6+8omega), leaving worst
deficit7beta-101/130. Actual signed ten-factor cancellation remains unproved.

Fresh primary-source audit rejects the Xiao--Li shifted-log-cutoff theorem as an
additive r2-correlation import and excludes withdrawn Kim2509.24152v4. Paid generic
decoupling and Kloosterman imports remain insufficient. Three reports, three external
seam reviews and conductor arithmetic-source review bind final hashes.

Identity State Patch:399 graph nodes and proof-draft bytes unchanged. No complete
moment or pointwise exponent improved. Full quarter and all M1/M2 parents remain open.
See strategy/gauss_circle_strategy_checkpoint_round208_2026-09-27.md and
rounds/codex-managed/gc-full-proof-signed-arithmetic-review/synthesis.md.
209 pending design; next mandatory broad strategy/literature review211.
'''
for p in ['state/project_summary.md','state/current_state.md','state/failure_ledger.md']:
 raw=Path(p).read_bytes();assert b'## Round208 complete strategy review (2026-09-27)' not in raw;put(p,raw+note.encode())
assert not subprocess.check_output(['git','diff','--name-only','--','rounds/obligation-main','rounds/web-research-test']).strip()
assert all(sha(p)==h for p,h in start.items())
validation=dict(preflight,campaign_id=cid,generated_at=now,terminal_label='costed_strategy_adjustment',
starting_graph_sha256=start[gp.as_posix()],final_graph_sha256=sha(gp),canonical_graph_sha256=hashlib.sha256(dump_graph(g).encode()).hexdigest(),
graph_nodes=399,original_graph_raw_bytes_unchanged=True,proof_draft_raw_bytes_unchanged=True,
previous_ledger_prefix_bytes_unchanged=True,legacy_paths_unchanged=True,next_strategy_checkpoint=211)
validation['status']='green_round208_strategy_closure_new_conditional_peak_gate_no_exponent_gain'
write(base/'controls/closure_validation.json',validation)
vtext=f'''# Round208 closure validation

GREEN for strategy closure and conditional bridge only; actual arithmetic target OPEN.
Graph SHA256:{sha(gp)}. Identity patch validated/applied in memory/reversed/replayed;
all399 graph nodes, graph/draft bytes and previous ledger prefix unchanged. Three reports,
three independent seam reviews, conductor source review and reconciliation, frozen inputs,
Round200--207 archive hashes and output hygiene passed. No exponent or complete moment gain.
Schema checks do not reprove historical mathematics. No mathematical numerical experiments.
209 pending design; next broad review211. Details:{base.as_posix()}/controls/closure_validation.json.
'''
for p in ['state/last_validation.md','state/last_validation_report.md']:put(p,vtext.encode())
assert not validate_graph(load_graph(gp),root=root) and not validate_campaign(read('state/active_campaign.yml'),g,root=root)
subprocess.run(['git','diff','--check'],check=True)
hashes={p.relative_to(root).as_posix():sha(p) for p in sorted((root/base).rglob('*')) if p.is_file() and p.name!='artifact_hashes.json' and '__pycache__' not in p.parts}
for p in [Path('strategy/round208_full_proof_strategy_review.md'),checkpoint]:hashes[p.as_posix()]=sha(p)
write(base/'controls/artifact_hashes.json',hashes)
print(json.dumps({k:validation[k] for k in ['status','graph_nodes','final_graph_sha256','proof_draft_raw_bytes_unchanged','conditional_bridge_changed_next_action','pointwise_exponent_change']},indent=2))
