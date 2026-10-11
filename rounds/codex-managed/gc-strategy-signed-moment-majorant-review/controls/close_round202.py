"""Validate the physical majorant lemma, close202, then record203 candidate."""
import copy, hashlib, json, re, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path
root=Path.cwd();sys.path.insert(0,str(root))
from math_collab.campaigns import validate_campaign,_next_campaign
from math_collab.proof_obligations import load_graph,dump_graph,write_graph,validate_graph,validate_patch_against_graph,apply_state_patch
cid='gc-strategy-signed-moment-majorant-review';base=Path('rounds/codex-managed')/cid
kernel=Path('proofs/kernels/gc_physical_twelfth_moment_absolute_majorant_obstruction.md')
candidate=base/'candidates/conductor_signed_convolution_interface.md'
strategy=Path('strategy/gauss_circle_strategy_checkpoint_round202_2026-09-23.md')
node_id='GC-physical-twelfth-moment-absolute-majorant-obstruction'
terminal='strategy_review_with_complete_signed_next_target'
now=datetime.now(timezone.utc).isoformat()
def read(p):return json.loads(Path(p).read_text(encoding='utf-8'))
def write(p,obj):Path(p).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
start=read(base/'controls/starting_state_hashes.json')
assert all(sha(p)==h for p,h in start.items()),'Protected starting input changed'
gp=Path('state/proof_obligations.yml');oldraw=gp.read_bytes();g=load_graph(gp)
assert len(g['proof_obligations'])==397
oldcanon=hashlib.sha256(dump_graph(g).encode()).hexdigest()
m=read('state/active_campaign.yml')
assert m['round_index']==202 and m['campaign_id']==cid and m['status']=='active'
assert not validate_graph(g,root=root) and not validate_campaign(m,g,root=root)
for t in m['tasks']:
 s=Path(t['report_path']).read_text(encoding='utf-8')
 assert all(re.search(rf'^## {i}\.',s,re.M) for i in range(1,8)),t['id']
reviews=[(base/'reviews/independent_physical_majorant_review.md',kernel),
         (base/'reviews/independent_signed_convolution_review.md',candidate)]
for p,artifact in reviews:
 s=p.read_text(encoding='utf-8')
 scoped_pass = ('GREEN' in s) if artifact==kernel else ('There is no doubtful step in (R2), (R3), or (R4)' in s)
 assert scoped_pass and sha(artifact).lower() in s.lower(),('review hash or scoped verdict',p)
 assert all(re.search(rf'^## {i}\.',s,re.M) for i in range(1,8)),p
judge=base/'reviews/conductor_round202_reconciliation.md'
assert 'GREEN for the physical termwise-majorant obstruction' in judge.read_text(encoding='utf-8')
assert strategy.is_file() and (base/'synthesis.md').is_file()
hygiene=[]
for p in [kernel,strategy,*base.rglob('*.md')]:
 s=p.read_text(encoding='utf-8')
 assert '\ufffd' not in s and not any(ord(c)<32 and c not in '\n\r\t' for c in s),p
 assert not re.search(r'\\\s*\{\s*\nm (?:odd|squarefree)',s),p
 hygiene.append(p.as_posix())
for previous in ['m9-m1-t1-complete-source-coefficient-mask-analysis','gc-whole-discrepancy-twelfth-moment']:
 archive=Path('rounds/codex-managed')/previous/'controls/artifact_hashes.json'
 for p,h in read(archive).items():assert sha(p)==h,('closed artifact changed',p)
protected=['GC-target','Conditional-bridge','M9','M9-M1','M9-M2','M9-endpoint-uniformity','GC-external-Li-Yang-theta-star','GC-weighted-square-root-exact-resonance-mass']
oldindex={n['id']:n for n in g['proof_obligations']}
assert set(protected)<=set(oldindex) and node_id not in oldindex
node=dict(id=node_id,type='lemma',track='proof_infrastructure',status='proved_internal',
 title='Actual nonzero near-resonance mass obstructs a termwise absolute twelfth-moment bound',
 statement_tex='Let Psi be fixed real even Schwartz with Psi(0)=1 and w nonzero nonnegative C_c^infinity((0,infinity)). For a_n(T)=r_2(n)n^(-3/4)Psi(sqrt(n/T)), there exist fixed0<a<b and h,c>0 such that for every sufficiently large realT, the actual coefficients are nonnegative on I_T=[aT,bT] intersect N, and T sum_(n_1,...,n_12 in I_T,0<|Delta|<=h/T) product_j a_(n_j)(T) Re w-hat(-TDelta)>=cT^(5/2), where Delta=sum_(j<=6)sqrt(n_j)-sum_(j>6)sqrt(n_j). All exact radical relations are removed using the uniform accepted absolute exact-mass bound. Consequently the full nonzero-frequency all-sign termwise absolute Fourier majorant (with prefactorT/2^12) is >=c_prime T^(5/2), so cannot be O_epsilon(T^(1+2eta+epsilon)) for everyepsilon>0 if eta<3/4. The proof uses elementary physical band mass and weighted six-root bins. For balanced2k with k>=4 the same method gives nonzero positive subsum >=c_k T^((k-1)/2); the conclusion is not asserted for k<=3 after exact deletion. This is strictly a majorant obstruction, not a lower bound for the complete signed displaced moment, and it disproves no actual moment target, M1/M2 estimate or pointwise exponent.',
 dependencies=['H1-H3','Divisor-bound-elementary','GC-weighted-square-root-exact-resonance-mass'],implies=[],blockers=[],
 evidence={'positive':[kernel.as_posix(),(base/'reports/blind_physical_near_resonance_mass.md').as_posix(),(base/'controls/conductor_round202_independent_analysis.md').as_posix(),reviews[0][0].as_posix(),judge.as_posix()],'negative':[],'inconclusive':[]},
 owner='Codex conductor',next_action='Retain the oscillatory Fourier window in the complete signed source. Any cutoff route must price the full actual tail and all mixed terms. This no-go does not reject the desired twelfth moment or supply any exponent improvement.')
patch=dict(round_index=202,campaign_id=cid,starting_graph_sha256=start[gp.as_posix()],
 proof_obligations=dict(create=[node],update=[],correct_rejected=[],reject=[],no_change=protected),
 round_assessment=dict(terminal_label=terminal,reason='Promote only the physical absolute-majorant obstruction; complete dated strategy/source/cutoff review and identify the complete signed filtered-convolution target. Actual moment, parent obligations and exponents remain unchanged.'),
 reversibility=dict(remove_created_ids=[node_id],rule='Delete sole created node to restore all prior structured graph data and canonical/original raw bytes. Replay from restored graph agrees except for new-node timestamp.'))
assert not validate_patch_against_graph(g,patch)
applied,result=apply_state_patch(copy.deepcopy(g),patch,round_index=202,judge_ref=judge.as_posix())
assert result.created==[node_id] and not result.updated and not result.rejected
assert applied['proof_obligations'][:-1]==g['proof_obligations']
assert all(applied[k]==g[k] for k in g if k!='proof_obligations')
assert not validate_graph(applied,root=root)
idx={n['id']:n for n in applied['proof_obligations']}
def walk(i,active,done):
 assert i in idx and i not in active,('dependency',i)
 if i in done:return
 active.add(i)
 for dep in idx[i].get('dependencies',[]):walk(dep,active,done)
 active.remove(i);done.add(i)
walk(node_id,set(),set())
assert all(idx[d]['status'] in ['proved_internal','proved_external_dependency'] for d in node['dependencies'])
assert all(Path(p).is_file() for p in node['evidence']['positive'])
restored=copy.deepcopy(applied);restored['proof_obligations']=[n for n in restored['proof_obligations'] if n['id']!=node_id]
assert restored==g
assert hashlib.sha256(dump_graph(restored).encode()).hexdigest()==oldcanon
newline='\r\n' if b'\r\n' in oldraw else '\n'
assert dump_graph(restored).replace('\n',newline).encode()==oldraw
replay,_=apply_state_patch(copy.deepcopy(restored),patch,round_index=202,judge_ref=judge.as_posix())
replay['proof_obligations'][-1]['last_updated_at']=applied['proof_obligations'][-1]['last_updated_at']
assert replay==applied
write(base/'state_patch.json',patch)
preflight=dict(round_index=202,status='green',graph_schema='pass',campaign_schema='pass',state_patch='pass',
 all_397_existing_nodes_and_other_graph_data_unchanged=True,new_dependency_cone='acyclic_and_accepted',
 reverse_original_raw_bytes='pass',replay_except_new_timestamp='pass',kernel_sha256=sha(kernel),
 signed_candidate_sha256=sha(candidate),utf8_hygiene_checked=hygiene,closed_round200_201_artifact_hashes='pass',
 actual_signed_target='open',exponent_change=False,mathematical_numerical_experiments=0)
write(base/'controls/promotion_preflight.json',preflight)
matrix=read('state/validation_matrix.yml')
for gate in matrix['gates']:
 if gate['id'].startswith('round202_'):gate['status']='green_stated_scope_only_signed_target_open'
for label,p in [('physical_kernel_review',reviews[0][0]),('signed_interface_review',reviews[1][0]),('patch_reverse_replay',base/'controls/promotion_preflight.json')]:
 matrix['gates'].append(dict(id='round202_'+label,status='green',artifact=p.as_posix()))
assert all(q['status'].startswith('green') and Path(q['artifact']).is_file() for q in matrix['gates'] if q['id'].startswith('round202_'))
matrix['promotion_status']='round_202_gates_green_physical_majorant_only_ready_to_apply'
write('state/validation_matrix.yml',matrix)
write_graph(gp,applied);assert load_graph(gp)==applied
finalhash=sha(gp)
matrix.update(promotion_status='round_202_closed_physical_majorant_only_no_exponent_change',graph_sha256=finalhash,analytic_target_status='open_complete_signed_filtered_convolution')
write('state/validation_matrix.yml',matrix)
draft=Path('state/best_proof_draft.md');assert sha(draft)==start[draft.as_posix()]
old=draft.read_text(encoding='utf-8')
addition='''
## Round 202 accepted physical absolute-majorant obstruction

The accepted node `GC-physical-twelfth-moment-absolute-majorant-obstruction`
proves that actual circle coefficients on a fixed positive band n~T
have a balanced, nonzero near-resonance subsum of real Fourier-weighted
size at least cT^(5/2), after every exact resonance has been deleted.
The physical coefficient mass T^(1/4), six-root bin count T^(3/2),
weighted Cauchy bound and accepted O(1) exact mass give the proof.
Consequently a termwise absolute all-sign Fourier majorant cannot
have scale T^(1+2eta+epsilon) for every epsilon>0 when eta<3/4.

This is only a no-go for that majorant. The complementary Fourier
terms remain signed, so the lower bound does not apply to the complete
displaced moment. The actual twelfth-moment target, every M1/M2 parent,
the quarter theorem, and all pointwise exponents remain unchanged.
The full proof and scope controls are in
`proofs/kernels/gc_physical_twelfth_moment_absolute_majorant_obstruction.md`.
'''
assert '## Round 202 accepted physical absolute-majorant obstruction' not in old
draft.write_text(old.rstrip()+'\n'+addition,encoding='utf-8')
assessment=dict(decision='promote_physical_majorant_obstruction_select_complete_signed_route',terminal_label=terminal,
 graph_mutation=True,main_result=patch['round_assessment']['reason'],resulting_graph_sha256=finalhash,
 patch_effect=f'1_create_0_update_0_correct_0_reject_{len(protected)}_no_change',exponent_change=False)
m.update(status='complete',completed_at=now,closing_assessment=assessment)
for t in m['tasks']:t['status']='completed'
m['post_report_reviews']=[p.as_posix() for p,_ in reviews]
assert not validate_campaign(m,applied,root=root);write('state/active_campaign.yml',m)
lp=Path('state/round_ledger.yml');s=lp.read_text(encoding='utf-8');ledger=json.loads(s)
assert ledger['active_round']==202 and ledger['rounds'][-1]['round_index']==202
entry=ledger['rounds'][-1];entry.update(status='closed',closing_assessment=assessment,completed_at=now,next_round=203)
for t in entry['tasks']:t['status']='completed'
pos=s.rfind('    {\n      "round_index": 202,');assert pos>0
last='\n'.join('    '+line for line in json.dumps(entry,indent=2,ensure_ascii=False).splitlines())
new=s[:pos]+last+'\n  ]\n}\n';assert json.loads(new)==ledger;lp.write_text(new,encoding='utf-8')

# Only after authoritative closure record the prospective successor objective.
write('state/next_round_plan.yml',dict(round_index=203,status='pending_design',campaign_id=None,
 starting_graph_sha256=finalhash,predecessor_round=202,predecessor_terminal_label=terminal,tasks=[],
 candidate_objective='Attack the complete actual signed filtered sixfold-convolution bound ||T chi-hat(T dot)*mu_(T,>T^(1/2047))^{*6}||_2 << T^(29/50+epsilon), with a rigorously bounded remainder for any smooth-density subtraction. No absolute-majorant substitution or omitted tail/mixed stratum.',
 full_goal_scope='A successful target would yield intermediate pointwise102/325 only; the quarter theorem requires further complete progress, for example sharp moments at arbitrarily high fixed orders.',
 design_constraint='Freeze a complete coefficient-sensitive analytic attempt, not another transform-only or positive-spacing gate. Keep all current source hypotheses, absolute-majorant no-go and residual interpolation boundary visible.',
 strategy_checkpoint=strategy.as_posix(),scheduled_review='Next mandatory broad strategy/current-literature review Round205 after202--204.'))
summary=_next_campaign(m,output_dir=base,graph_hash=finalhash)
summary+='\n## Closing decision\n\nThe physical absolute-majorant obstruction is accepted; the complete signed moment remains open. Round203 is pending design on the complete filtered convolution. Next broad strategy review: Round205.\n'
for p in ['state/current_round.md','state/next_campaign.md']:Path(p).write_text(summary,encoding='utf-8')
note='''
## Round 202 strategy checkpoint and physical majorant boundary (2026-09-23)

The scheduled current-primary-literature and full-frontier review is
complete. One actual-coefficient lemma proves that termwise absolute
twelfth-moment estimation retains at least T^(5/2), even after exact
resonance removal. It does not lower-bound the full signed moment.
Checked residual interpolation gives no new saving. No external theorem,
existing graph node or exponent changed. The next candidate is the
complete signed filtered-convolution bound, with all tails retained.
See `strategy/gauss_circle_strategy_checkpoint_round202_2026-09-23.md`
and `rounds/codex-managed/gc-strategy-signed-moment-majorant-review/synthesis.md`.
Round203 is pending design; the next scheduled strategy review is205.
'''
for p in ['state/project_summary.md','state/current_state.md']:
 q=Path(p);s=q.read_text(encoding='utf-8');assert '## Round 202 strategy checkpoint' not in s
 q.write_text(s.rstrip()+'\n'+note,encoding='utf-8')
assert sha('strategy/gauss_circle_strategy_review_2026-09-23.md')==start['strategy/gauss_circle_strategy_review_2026-09-23.md']
assert not subprocess.check_output(['git','diff','--name-only','--','rounds/obligation-main','rounds/web-research-test']).strip()
validation=dict(preflight,status='green_round202_closure_majorant_only',campaign_id=cid,generated_at=now,
 terminal_label=terminal,starting_graph_sha256=start[gp.as_posix()],starting_canonical_sha256=oldcanon,
 final_graph_sha256=finalhash,graph_nodes=len(applied['proof_obligations']),new_nodes=[node_id],
 proof_draft_appended_only_after_valid_graph=True,final_proof_draft_sha256=sha(draft),
 mandatory_strategy_review_complete=True,next_strategy_checkpoint=205,legacy_paths_unchanged=True)
write(base/'controls/closure_validation.json',validation)
text=(f'# Round202 closure validation\n\nStatus: GREEN for physical majorant lemma and strategy review; complete signed target OPEN.\n\n'
 f'Graph SHA256: `{finalhash}`. One new internal lemma; all397 prior nodes and all other graph data unchanged. '
 'Exact-hash independent reviews, graph/campaign validation, accepted dependency cone, protected archives, '
 'original-byte restoration and replay excluding only the new timestamp passed. Applicable gates were green '
 'before graph mutation; the proof draft was appended afterward. No numerical experiment or exponent change.\n\n'
 'Round203 is pending design on the complete signed filtered convolution. Next scheduled global strategy/literature review:205.\n\n'
 f'Details: `{base.as_posix()}/controls/closure_validation.json`.\n')
for p in ['state/last_validation.md','state/last_validation_report.md']:Path(p).write_text(text,encoding='utf-8')
assert not validate_graph(load_graph(gp),root=root) and not validate_campaign(read('state/active_campaign.yml'),applied,root=root)
subprocess.run(['git','diff','--check'],check=True)
hashes={p.relative_to(root).as_posix():sha(p) for p in sorted((root/base).rglob('*')) if p.is_file() and p.name!='artifact_hashes.json' and '__pycache__' not in p.parts}
hashes.update({kernel.as_posix():sha(kernel),strategy.as_posix():sha(strategy)})
write(base/'controls/artifact_hashes.json',hashes)
print(json.dumps({k:validation[k] for k in ['status','graph_nodes','new_nodes','final_graph_sha256','exponent_change']},indent=2))
