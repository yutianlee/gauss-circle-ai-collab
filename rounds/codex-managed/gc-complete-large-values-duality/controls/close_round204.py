"""Validate the complete large-values lemma before closing Round204."""
import copy
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

root = Path.cwd()
sys.path.insert(0, str(root))
from math_collab.campaigns import validate_campaign, _next_campaign
from math_collab.proof_obligations import (
    load_graph, dump_graph, write_graph, validate_graph,
    validate_patch_against_graph, apply_state_patch,
)

cid = 'gc-complete-large-values-duality'
base = Path('rounds/codex-managed') / cid
kernel = Path('proofs/kernels/gc_complete_square_root_large_values_moment_bound.md')
kernel_hash = '942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212'
node_id = 'GC-complete-square-root-large-values-moment-bound'
terminal = 'complete_distribution_gain_target_open'
now = datetime.now(timezone.utc).isoformat()

def read(p):
    return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def write(p, obj):
    Path(p).write_text(json.dumps(obj, indent=2, ensure_ascii=False)+'\n', encoding='utf-8', newline='\n')
def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def seven_sections(p):
    text = Path(p).read_text(encoding='utf-8')
    assert all(re.search(rf'^## {i}\.', text, re.M) for i in range(1, 8)), p
    return text

start = read(base/'controls/starting_state_hashes.json')
assert all(sha(p) == h for p, h in start.items()), 'Starting state changed'
for p, h in read(base/'controls/frozen_artifact_hashes.json').items():
    assert sha(p) == h, ('Frozen artifact changed', p)
prior_campaigns = [
    'm9-m1-t1-complete-source-coefficient-mask-analysis',
    'gc-whole-discrepancy-twelfth-moment',
    'gc-strategy-signed-moment-majorant-review',
    'gc-complete-signed-convolution-attack',
]
for prior in prior_campaigns:
    for p, h in read(Path('rounds/codex-managed')/prior/'controls/artifact_hashes.json').items():
        assert sha(p) == h, ('Closed artifact changed', p)
assert sha(kernel) == kernel_hash
pause = read(base/'controls/paused_checkpoint.json')
for p, h in pause['artifact_sha256'].items():
    if '/reports/' in p:
        assert sha(p) == h, ('Original completed report changed', p)

gp = Path('state/proof_obligations.yml')
oldraw = gp.read_bytes()
g = load_graph(gp)
oldcanon = hashlib.sha256(dump_graph(g).encode()).hexdigest()
assert len(g['proof_obligations']) == 398
assert not validate_graph(g, root=root)
m = read('state/active_campaign.yml')
assert m['round_index'] == 204 and m['campaign_id'] == cid and m['status'] == 'active'
assert not validate_campaign(m, g, root=root)
frozen = read(base/'plan.json')['campaign']
for key in ['frozen_target', 'completion_criteria', 'resource_policy', 'controls', 'target_obligations', 'review_seams']:
    assert m[key] == frozen[key], ('Frozen scope changed', key)
for task, original in zip(m['tasks'], frozen['tasks']):
    assert {k: v for k, v in task.items() if k != 'status'} == {k: v for k, v in original.items() if k != 'status'}
    seven_sections(task['report_path'])
assert len(m['tasks']) == len(frozen['tasks']) == 3

reviews = [base/'reviews'/f'{name}.md' for name in [
    'gram_tail_seam_review', 'source_correlation_seam_review', 'sharp_moment_seam_review',
]]
for p in reviews:
    text = seven_sections(p)
    scoped_pass = ('PASS for the revised artifact' in text) if p.stem == 'gram_tail_seam_review' else ('GREEN' in text)
    assert scoped_pass and kernel_hash in text.lower(), ('Exact-hash scoped verdict absent', p)
judge = base/'reviews/conductor_round204_reconciliation.md'
judgment = seven_sections(judge)
assert 'GREEN for the complete weaker distribution and moment consequences' in judgment
assert kernel_hash in judgment.lower()
assert (base/'synthesis.md').is_file()
assert (base/'controls/conductor_round204_independent_analysis.md').is_file()
assert (base/'controls/resume_validation.json').is_file()
hygiene = []
for p in [kernel, *base.rglob('*.md')]:
    text = p.read_text(encoding='utf-8')
    assert '\ufffd' not in text and not any(ord(c) < 32 and c not in '\n\r\t' for c in text), p
    hygiene.append(p.as_posix())
assert not subprocess.check_output(['git', 'diff', '--name-only', '--', 'rounds/obligation-main', 'rounds/web-research-test']).strip()
subprocess.run(['git', 'diff', '--check'], check=True)

protected = [
    'GC-target', 'Conditional-bridge', 'M9', 'M9-M1', 'M9-M2', 'M9-endpoint-uniformity',
    'GC-external-Li-Yang-theta-star', 'Bourgain-2017-reciprocal-exponent-pair-source-audit',
    'GC-weighted-square-root-exact-resonance-mass',
    'GC-physical-twelfth-moment-absolute-majorant-obstruction',
]
oldindex = {n['id']: n for n in g['proof_obligations']}
assert set(protected) <= set(oldindex) and node_id not in oldindex
node = dict(
    id=node_id, type='lemma', track='proof_infrastructure', status='proved_internal',
    title='Complete square-root large-value distribution and improved recorded circle moments',
    statement_tex=(
        'For fixed real even Schwartz Psi, fixed bounded measurable nonnegative w supported in [c,C] subset (0,infinity), '
        'real T>=2 and every real U>=0, let B_(T,U)(R)=sum_(n>U)r_2(n)n^(-3/4)Psi(sqrt(n/T))cos(2pi R sqrt(n)-3pi/4). '
        'Uniformly in U and V>=1, D_(T,U)(V)=integral w(R/T)1_(|B_(T,U)|>V)dR '
        '<<_epsilon T^epsilon(V^(-2)+T V^(-136/13)). The proof includes singleton n=1, all partial dyadic blocks, '
        'the infinite Schwartz tail, the exact Gram diagonal and the full localization ceiling. '
        'For Psi the Fourier transform of a fixed nonnegative real radial smooth unit-mass mollifier supported in the unit disk, '
        'theta=theta_LY and beta=2theta-1/2, every fixed p>=2 satisfies '
        'integral w(R/T)|B_(T,0)(R)|^p dR <<_(p,epsilon) T^(1+epsilon)+T^((p-2)beta+epsilon). '
        'The same moment bound holds for U=floor(T^(1/2047)), not asserted uniformly for all U. '
        'For the inclusive sharp discrepancy and real Y>=4, integral_(Y/2)^(3Y)|P(x)|^p dx '
        '<<_(p,epsilon)Y^(1+p/4+epsilon)+Y^(1+(p-2)theta+epsilon). '
        'In particular p=12 gives Y^(1+10theta+epsilon), normalized sixth-power norm T^(5beta+epsilon), '
        'and the conjectural-order moment endpoint q_star=2+1/beta>262/27. '
        'This improves the recorded project moment comparison without a novelty claim. '
        'It does not prove the stronger Round204 distribution, any M1/M2 parent, a better pointwise exponent or the quarter theorem. '
        'The aligned arbitrary-coefficient control explains the generic diagonal term; it is not an arithmetic counterexample.'
    ),
    dependencies=['H1-H3', 'Divisor-bound-elementary', 'Bourgain-2017-reciprocal-exponent-pair-source-audit', 'GC-external-Li-Yang-theta-star'],
    implies=[], blockers=[],
    evidence=dict(positive=[kernel.as_posix(),
        *[t['report_path'] for t in m['tasks']], *[p.as_posix() for p in reviews],
        (base/'controls/conductor_round204_independent_analysis.md').as_posix(), judge.as_posix()],
        negative=[], inconclusive=[]),
    owner='Codex conductor',
    next_action='At the next scheduled strategy review, compare complete arithmetic routes to improve the remaining high values. The generic coefficient norm and correlation estimate do not remove the V^-2 term. Preserve the full quarter target and unchanged source qualifications.',
)
patch = dict(
    round_index=204, campaign_id=cid, starting_graph_sha256=start[gp.as_posix()],
    proof_obligations=dict(create=[node], update=[], correct_rejected=[], reject=[], no_change=protected),
    round_assessment=dict(terminal_label=terminal, reason='Promote a complete actual distribution and its improved recorded moment consequences; retain the frozen stronger distribution and all pointwise/parent targets as open.'),
    reversibility=dict(remove_created_ids=[node_id], rule='Remove the sole created node to restore all prior structured graph data and canonical/original raw bytes. Replay agrees except for the new-node timestamp.'),
)
assert not validate_patch_against_graph(g, patch)
applied, result = apply_state_patch(copy.deepcopy(g), patch, round_index=204, judge_ref=judge.as_posix())
assert result.created == [node_id] and not result.updated and not result.rejected and not result.corrected_rejected
assert applied['proof_obligations'][:-1] == g['proof_obligations']
assert all(applied[k] == g[k] for k in g if k != 'proof_obligations')
assert not validate_graph(applied, root=root)
idx = {n['id']: n for n in applied['proof_obligations']}
done = set()
def walk(i, active):
    assert i in idx and i not in active, ('New dependency cone cycle or missing node', i)
    if i in done:
        return
    assert idx[i]['status'] in ['proved_internal', 'proved_external_dependency'], ('Unaccepted dependency', i)
    active.add(i)
    for dep in idx[i].get('dependencies', []):
        walk(dep, active)
    active.remove(i)
    done.add(i)
walk(node_id, set())
assert all(Path(p).is_file() for p in node['evidence']['positive'])
restored = copy.deepcopy(applied)
restored['proof_obligations'] = [n for n in restored['proof_obligations'] if n['id'] != node_id]
assert restored == g and hashlib.sha256(dump_graph(restored).encode()).hexdigest() == oldcanon
newline = '\r\n' if b'\r\n' in oldraw else '\n'
assert dump_graph(restored).replace('\n', newline).encode() == oldraw
replay, _ = apply_state_patch(copy.deepcopy(restored), patch, round_index=204, judge_ref=judge.as_posix())
replay['proof_obligations'][-1]['last_updated_at'] = applied['proof_obligations'][-1]['last_updated_at']
assert replay == applied
write(base/'state_patch.json', patch)
preflight = dict(
    round_index=204, status='green', graph_schema='pass', campaign_schema='pass', state_patch='pass',
    all_398_existing_nodes_and_other_graph_data_unchanged=True,
    new_dependency_cone='acyclic_and_all_nodes_accepted', dependency_cone=sorted(done),
    reverse_original_raw_bytes='pass', replay_except_new_timestamp='pass',
    kernel_sha256=kernel_hash, review_hashes={p.as_posix(): sha(p) for p in reviews},
    frozen_scope_and_briefs_unchanged=True, closed_round200_through203_artifacts_unchanged=True,
    original_reports_unchanged=True, singleton_repair='reviewed', utf8_hygiene=hygiene,
    mathematical_numerical_experiments=0, complete_weaker_distribution='proved',
    frozen_stronger_distribution='open', moment_comparison_improved=True, pointwise_exponent_change=False,
    validation_scope='New claim and its accepted dependency cone only; historical graph mathematics and inherited legacy advisories are not globally recertified.',
)
write(base/'controls/promotion_preflight.json', preflight)
matrix = read('state/validation_matrix.yml')
for gate in matrix['gates']:
    if gate['id'].startswith('round204_'):
        gate['status'] = 'green_stated_scope_only_stronger_target_open'
for p in reviews:
    matrix['gates'].append(dict(id='round204_'+p.stem, status='green', artifact=p.as_posix()))
matrix['gates'].append(dict(id='round204_patch_reverse_replay', status='green', artifact=(base/'controls/promotion_preflight.json').as_posix()))
assert all(gate['status'].startswith('green') and Path(gate['artifact']).is_file() for gate in matrix['gates'] if gate['id'].startswith('round204_'))
matrix['promotion_status'] = 'round_204_gates_green_complete_weaker_bound_ready_to_apply'
write('state/validation_matrix.yml', matrix)

# All required gates are green. This is the only mathematical-state mutation.
assert gp.read_bytes() == oldraw
write_graph(gp, applied)
assert load_graph(gp) == applied
finalhash = sha(gp)
matrix.update(
    promotion_status='round_204_closed_complete_weaker_bound_moment_gain_only', graph_sha256=finalhash,
    analytic_target_status='open_complete_stronger_high_value_distribution',
    decision_rule='Round204 adds one reviewed complete large-values/moment lemma. All398 prior nodes and pointwise exponents remain unchanged. Round205 is the mandatory broad strategy/current-literature review.',
)
write('state/validation_matrix.yml', matrix)
draft = Path('state/best_proof_draft.md')
assert sha(draft) == start[draft.as_posix()]
draft_raw = draft.read_bytes()
addition = '''
## Round 204 accepted complete large-values and moment bound

The accepted node `GC-complete-square-root-large-values-moment-bound`
proves D_(T,U)(V)<<T^epsilon(V^-2+T V^(-136/13)) for the full
smoothed square-root series, uniformly in every lower cutoff U>=0
and V>=1. Its finite Gram proof retains the diagonal and the full
localization ceiling. The proof includes n=1, all partial blocks
and the complete infinite upper tail. The external pair acts only
on the unweighted correlation kernel, with its exact square-root
derivative class and all small-parameter regimes separately checked.

For the radial mollifier and theta=theta_LY, beta=2theta-1/2, the
full normalized p-moment is bounded by T^(1+epsilon) plus
T^((p-2)beta+epsilon), for every fixed p>=2. The sharp inclusive
discrepancy therefore has p-moment at most Y^(1+p/4+epsilon) plus
Y^(1+(p-2)theta+epsilon). At p=12 this is Y^(1+10theta+epsilon);
the conjectural-order moment endpoint is2+1/beta>262/27.

This is an improvement of the project's recorded moment comparison;
no novelty or pointwise exponent improvement is claimed. The resulting
p=12 persistence exponent(1+10theta)/13 is larger than theta. The
frozen stronger high-value target remains open above its proved
initial range; the full quarter theorem and all M1/M2 parents remain
open. The aligned generic coefficient example does not refute the
actual arithmetic target. See the complete reviewed proof in
`proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`.
'''
assert b'## Round 204 accepted complete large-values and moment bound' not in draft_raw
draft.write_bytes(draft_raw+addition.encode('utf-8'))
assert draft.read_bytes().startswith(draft_raw)
assessment = dict(
    decision='promote_complete_large_values_and_moment_bound_only', terminal_label=terminal,
    graph_mutation=True, main_result=patch['round_assessment']['reason'], resulting_graph_sha256=finalhash,
    patch_effect=f'1_create_0_update_0_correct_0_reject_{len(protected)}_no_change',
    moment_comparison_improved=True, pointwise_exponent_change=False,
)
m.update(status='complete', completed_at=now, closing_assessment=assessment,
         post_report_reviews=[p.as_posix() for p in reviews])
assert not validate_campaign(m, applied, root=root)
write('state/active_campaign.yml', m)
lp = Path('state/round_ledger.yml')
s = lp.read_text(encoding='utf-8')
ledger = json.loads(s)
assert ledger['active_round'] == 204 and ledger['rounds'][-1]['round_index'] == 204
old_entries = copy.deepcopy(ledger['rounds'][:-1])
entry = ledger['rounds'][-1]
entry.update(status='closed', closing_assessment=assessment, completed_at=now, next_round=205)
for task in entry['tasks']:
    task['status'] = 'completed'
pos = s.rfind('    {\n      "round_index": 204,')
assert pos > 0
new = s[:pos]+'\n'.join('    '+line for line in json.dumps(entry, indent=2, ensure_ascii=False).splitlines())+'\n  ]\n}\n'
assert json.loads(new) == ledger and ledger['rounds'][:-1] == old_entries
lp.write_text(new, encoding='utf-8', newline='\n')

# Only after the recorded closure, identify the required successor review.
write('state/next_round_plan.yml', dict(
    round_index=205, status='pending_design', campaign_id=None, starting_graph_sha256=finalhash,
    predecessor_round=204, predecessor_terminal_label=terminal, tasks=[],
    candidate_objective='Perform the mandatory broad strategy and current-primary-literature review after Rounds202--204; assess the complete new moment bound against the full quarter target and select one quantified complete arithmetic objective.',
    design_constraint='Reassess all full-proof frontiers, including complete-source M1/M2 routes and the whole-discrepancy route. Do not repeat generic diagonal removal or termwise absolute majorants. Test exact source hypotheses and restored powers before selecting a method.',
    current_moment_bound='Sharp moment Y^(1+p/4+epsilon)+Y^(1+(p-2)theta_LY+epsilon) for every fixed p>=2; twelfth moment Y^(1+10theta_LY+epsilon).',
    remaining_quantitative_gap='Frozen radius moment29/25 versus10beta; generic distribution ceases to certify the target above V=T^(13/125). Complete arithmetic high values remain open.',
    full_goal_scope='P(X)<<X^(1/4+epsilon) remains the objective. The new moments tend only to the inherited theta under the current persistence bridge.',
    scheduled_review='Round205 mandatory before the next analytic campaign; review current literature as of execution date.',
))
summary = _next_campaign(m, output_dir=base, graph_hash=finalhash)
summary += '\n## Closing decision\n\nOne complete distribution/moment lemma accepted. All prior graph nodes and pointwise exponents unchanged; the stronger arithmetic high-value target is open. Round205 is pending design for the mandatory broad strategy/current-literature review.\n'
for p in ['state/current_round.md', 'state/next_campaign.md']:
    Path(p).write_text(summary, encoding='utf-8', newline='\n')
note = '''
## Round 204 complete distribution and moment gain (2026-09-26)

The complete actual large-value bound D(V)<<T^epsilon(V^-2+TV^(-136/13))
is accepted with all tails, endpoints and the diagonal retained. It gives
the sharp twelfth moment Y^(1+10theta_LY+epsilon), improving the project's
recorded moment comparison. It does not improve the pointwise exponent.
The full high-value target remains open; its generic envelope is insufficient
above V=T^(13/125). One accepted node was added; all398 prior nodes remain
unchanged. No numerical experiment, new external theorem, or novelty claim.
See `rounds/codex-managed/gc-complete-large-values-duality/synthesis.md`.
Round205 is pending design for the mandatory broad strategy/current-literature
review after202--204. The full quarter goal remains active and unproved.
'''
for p in ['state/project_summary.md', 'state/current_state.md']:
    path = Path(p)
    old = path.read_bytes()
    assert b'## Round 204 complete distribution and moment gain' not in old
    path.write_bytes(old+note.encode('utf-8'))
failure_note = '''
## Round 204 scope boundary: generic large values do not close arithmetic high values

The accepted complete envelope retains V^-2 from a single localization
interval and the finite Gram diagonal. An aligned arbitrary coefficient
vector attains that scale and its twelfth moment T^(10beta). This is not
an arithmetic r2 counterexample. The actual target remains open above
the range certified by both terms, V<=T^(13/125). A weighted-Gram
Stieltjes attempt preserves the phase derivative and pays |u|N^theta;
the accepted pointwise bound alone does not improve that oscillatory
remainder. Record this attempt without ruling out arithmetic cancellation.
Evidence: `rounds/codex-managed/gc-complete-large-values-duality/synthesis.md`.
'''
fl = Path('state/failure_ledger.md')
assert b'## Round 204 scope boundary' not in fl.read_bytes()
fl.write_bytes(fl.read_bytes()+failure_note.encode('utf-8'))

assert sha('strategy/gauss_circle_strategy_review_2026-09-23.md') == start['strategy/gauss_circle_strategy_review_2026-09-23.md']
validation = dict(preflight, status='green_round204_closure_complete_moment_gain_only',
    campaign_id=cid, generated_at=now, terminal_label=terminal,
    starting_graph_sha256=start[gp.as_posix()], starting_canonical_sha256=oldcanon,
    final_graph_sha256=finalhash, graph_nodes=len(applied['proof_obligations']), new_nodes=[node_id],
    proof_draft_appended_only_after_valid_graph=True, old_proof_draft_bytes_preserved=True,
    final_proof_draft_sha256=sha(draft), all_previous_ledger_entries_unchanged=True,
    legacy_paths_unchanged=True, next_strategy_checkpoint=205,
)
write(base/'controls/closure_validation.json', validation)
validation_text = (
    '# Round204 closure validation\n\n'
    'GREEN for the complete weaker distribution and moment consequences; stronger arithmetic target OPEN.\n\n'
    f'Graph SHA256: `{finalhash}`. One new internal lemma; all398 prior nodes and all other graph data are unchanged. '
    'Three original reports, a statement-only rederivation, three exact-hash seam reviews, singleton repair, '
    'accepted dependency-cone validation, protected Round200--203 archive hashes, original-byte reversal '
    'and replay excluding only the new timestamp passed. Required gates were green before graph mutation; '
    'the proof draft was appended afterward with its old bytes preserved.\n\n'
    'Scope: no new pointwise exponent, no quarter proof, no global recertification of historical mathematics '
    'or removal of inherited legacy advisories, and no mathematical numerical experiment. '
    'Round205 is pending design for the mandatory broad strategy/current-literature review.\n\n'
    f'Details: `{base.as_posix()}/controls/closure_validation.json`.\n'
)
for p in ['state/last_validation.md', 'state/last_validation_report.md']:
    Path(p).write_text(validation_text, encoding='utf-8', newline='\n')
assert not validate_graph(load_graph(gp), root=root)
assert not validate_campaign(read('state/active_campaign.yml'), applied, root=root)
assert not subprocess.check_output(['git', 'diff', '--name-only', '--', 'rounds/obligation-main', 'rounds/web-research-test']).strip()
subprocess.run(['git', 'diff', '--check'], check=True)
hashes = {p.relative_to(root).as_posix(): sha(p) for p in sorted((root/base).rglob('*'))
          if p.is_file() and p.name != 'artifact_hashes.json' and '__pycache__' not in p.parts}
strategy = Path('strategy/round204_complete_large_values_attack.md')
hashes.update({kernel.as_posix(): sha(kernel), strategy.as_posix(): sha(strategy)})
write(base/'controls/artifact_hashes.json', hashes)
print(json.dumps({k: validation[k] for k in ['status', 'graph_nodes', 'new_nodes', 'final_graph_sha256', 'pointwise_exponent_change']}, indent=2))
