"""Close217 with a create-only, fully reviewed absolute-certificate obstruction."""
import copy
import hashlib
import json
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

root = Path.cwd()
sys.path.insert(0, str(root))
from math_collab.campaigns import validate_campaign, _next_campaign
from math_collab.proof_obligations import (
    load_graph, dump_graph, write_graph, validate_graph,
    validate_patch_against_graph, apply_state_patch,
)

cid = 'gc-full-goal-distinct-source-review'
base = Path('rounds/codex-managed') / cid
gp = Path('state/proof_obligations.yml')
draft = Path('state/best_proof_draft.md')
candidate = base / 'controls/conductor_distinct_absolute_certificate.md'
kernel = Path('proofs/kernels/gc_distinct_radical_absolute_certificate_obstruction.md')
node_id = 'GC-distinct-radical-absolute-certificate-obstruction'
checkpoint = Path('strategy/gauss_circle_strategy_checkpoint_round217_2026-09-28.md')
judge = base / 'reviews/conductor_round217_reconciliation.md'
now = datetime.now(timezone.utc).isoformat()


def read(p):
    return json.loads(Path(p).read_text(encoding='utf-8-sig'))


def put(p, data):
    for attempt in range(5):
        try:
            Path(p).write_bytes(data)
            return
        except OSError:
            if attempt == 4:
                raise
            time.sleep(.2)


def write(p, obj):
    put(p, (json.dumps(obj, indent=2, ensure_ascii=False) + '\n').encode())


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def contract(p):
    s = Path(p).read_text(encoding='utf-8')
    assert all(re.search(rf'^#{{1,2}} {i}\.', s, re.M) for i in range(1, 8)), p
    return s


start = read(base / 'controls/starting_state_hashes.json')
assert all(sha(p) == h for p, h in start.items())
for p, h in read(base / 'controls/frozen_artifact_hashes.json').items():
    assert sha(p) == h, ('frozen', p)
ledger_initial = read('state/round_ledger.yml')
priors = [e for e in ledger_initial['rounds'] if 200 <= e['round_index'] <= 216]
assert len(priors) == 17 and all(e['status'] == 'closed' for e in priors)
archive_count = 0
for e in priors:
    for p, h in read(Path('rounds/codex-managed') / e['campaign_id'] / 'controls/artifact_hashes.json').items():
        assert sha(p) == h, ('prior archive', p)
        archive_count += 1
assert archive_count == 402, archive_count

oldraw = gp.read_bytes()
old_draft = draft.read_bytes()
g = load_graph(gp)
oldcanon = hashlib.sha256(dump_graph(g).encode()).hexdigest()
assert len(g['proof_obligations']) == 400 and not validate_graph(g, root=root)
m = read('state/active_campaign.yml')
assert m['round_index'] == 217 and m['campaign_id'] == cid and m['status'] == 'active'
assert not validate_campaign(m, g, root=root)
frozen = read(base / 'plan.json')['campaign']
for key in ['frozen_target', 'completion_criteria', 'resource_policy', 'controls', 'target_obligations', 'review_seams']:
    assert m[key] == frozen[key], key
assert len(m['tasks']) == len(frozen['tasks']) == 3
for task, original in zip(m['tasks'], frozen['tasks']):
    assert {k: v for k, v in task.items() if k != 'status'} == {k: v for k, v in original.items() if k != 'status'}
    contract(task['report_path'])

fixed = {
    'reports/distinct_correlation_sources.md': '45ec295cc04a23d061f7278015327af9ff7e4884c902c05319fb3629ed64bc59',
    'reports/full_frontier_sources.md': '3fcd969a5fb4b53edb6cbbd337b19ae18c363fb44bc1cdc0042a80f05c1fd338',
    'reports/blind_moment_family.md': 'fe681f61a48faac2825138c8b7e0884e4f73c05b6cca789cb0f72b9f33e49e35',
    'controls/conductor_distinct_absolute_certificate.md': '603aa69cb4b757707d6eb89bb8290b05190b6b6d5cae83be52ddc19658ef68bb',
    'controls/conductor_distinct_frequency_control.md': '9ac60977966c4368427daa62a4ebd16ac7e56ca60b291e02186a26d81cea4efa',
    'reviews/independent_distinct_certificate_review.md': '314c3592a935764a00c812ad356489263c08cebc179261a1f63c7c696633fffe',
    'reviews/independent_distinct_sources_review.md': '49b50c16d7f20d531daafc0e140ee2f6fbed755b4176c1034b4a13d9b6237797',
    'reviews/independent_moment_family_review.md': '610dd05fde201087ed70f4d1b6898705e8952bc2c03b92393aff7e7b63b9d404',
    'reviews/isolated_distinct_certificate_rederivation.md': 'bf78fb97f423722a38caf3ff7966758d112a4f2f3166c200d4ba02f75f44e8bd',
}
for rel, h in fixed.items():
    assert sha(base / rel) == h, ('final frozen artifact', rel)
packet = base / 'briefs/isolated_distinct_certificate_statement.md'
isolated = base / 'reviews/isolated_distinct_certificate_rederivation.md'
assert sha(packet) == '23962eb512ba6f2183581e8c356e95007b16ae91f624ed4cd04779aa1b7c442d'
assert 'No claimant proof, graph, ledger, strategy' in contract(isolated)
reviews = [
    (base / 'reviews/independent_distinct_certificate_review.md', [candidate, base / 'controls/conductor_distinct_frequency_control.md']),
    (base / 'reviews/independent_distinct_sources_review.md', [base / 'reports/distinct_correlation_sources.md']),
    (base / 'reviews/independent_moment_family_review.md', [base / 'reports/blind_moment_family.md']),
    (base / 'reviews/conductor_full_frontier_source_review.md', [base / 'reports/full_frontier_sources.md']),
    (base / 'reviews/conductor_moment_family_binding.md', [base / 'reports/blind_moment_family.md', base / 'reports/full_frontier_sources.md']),
]
for p, artifacts in reviews:
    s = contract(p)
    assert 'GREEN' in s, p
    for a in artifacts:
        assert sha(a) in s.lower(), ('review binding', p, a)
all_reviews = [p for p, _ in reviews] + [isolated]
decision = read(base / 'controls/closing_decision.json')
assert decision['graph_mutation'] is True
assert not decision['complete_moment_bound_improved'] and not decision['pointwise_exponent_change']
contract(base / 'synthesis.md')
controls = [candidate, base / 'controls/conductor_distinct_frequency_control.md', base / 'controls/conductor_current_source_status.md']
for p in controls:
    contract(p)
evidence = [Path(t['report_path']) for t in m['tasks']] + controls + [packet] + all_reviews + [checkpoint, base / 'synthesis.md']
bindings = '\n'.join(f'- `{p.as_posix()}`: `{sha(p)}`.' for p in evidence)
s = contract(judge)
if 'FINAL_HASH_BINDINGS' in s:
    put(judge, s.replace('FINAL_HASH_BINDINGS', bindings).encode())
else:
    assert bindings in s
assert 'GREEN for the distinct-class absolute-certificate obstruction only' in contract(judge)
if kernel.exists():
    assert kernel.read_bytes() == candidate.read_bytes()
else:
    put(kernel, candidate.read_bytes())
assert sha(kernel) == fixed['controls/conductor_distinct_absolute_certificate.md']
for p in [kernel, checkpoint, *base.rglob('*.md')]:
    raw = p.read_bytes()
    s = raw.decode('utf-8')
    assert not re.search(rb'\r(?!\n)', raw), p
    assert '\ufffd' not in s and not any(ord(c) < 32 and c not in '\n\r\t' for c in s), p
assert not subprocess.check_output(['git', 'diff', '--name-only', '--', 'rounds/obligation-main', 'rounds/web-research-test']).strip()
subprocess.run(['git', 'diff', '--check'], check=True)

protected = ['GC-target', 'Conditional-bridge', 'M9', 'M9-M1', 'M9-M2', 'M9-endpoint-uniformity',
             'GC-external-Li-Yang-theta-star', 'GC-weighted-square-root-exact-resonance-mass',
             'GC-complete-square-root-large-values-moment-bound', 'GC-complete-distinct-radical-twelfth-reduction']
assert node_id not in {n['id'] for n in g['proof_obligations']}
node = dict(
    id=node_id, type='lemma', track='proof_infrastructure', status='proved_internal',
    title='Actual distinct-radical termwise absolute Fourier certificate obstruction',
    statement_tex=(
        'Fix a nonnegative real radial smooth unit-mass mollifier supported in the unit disk, '
        'Psi(s)=rho-hat(s e1), a nonnegative smooth w supported in [1/2,2] with positive integral, '
        'fixed even p=2k>=4 and fixed 0<=alpha<1. For real T sufficiently large set '
        'Q=floor(T^alpha), a_n=r2(n)n^(-3/4)Psi(sqrt(n/T)). Choose fixed c>0 small enough '
        'that Psi>=1/2 on sqrt(c)<=s<=sqrt(2c), and retain integers N_T={cT<=n<=2cT:sf(n)>Q}. '
        'Then T 2^(-p) sum_(ordered n_1,...,n_p in N_T; sf(n_i) pairwise distinct) '
        'product_i a_(n_i) |w-hat(-T[sum_(i<=k)sqrt(n_i)-sum_(i>k)sqrt(n_i)])| '
        '>=c_(p,alpha,rho,w) T^(p/4-1/2). This is a positive subcollection of the complete '
        'termwise absolute distinct-class Fourier expansion. Its proof retains actual coefficients, '
        'all harmonics in the selected block, all repeated-class exclusion, ordered multiplicities '
        'and real endpoints. Distinct squarefree classes make each retained frequency nonzero. '
        'At p=12,alpha=2/5 the lower bound T^(5/2) rules out closing the29/25 target by '
        'this termwise absolute certificate. It is not a lower bound for signed I_p or any physical '
        'moment, does not reject the signed target or quarter theorem, and is not uniform for p growing with T.'
    ),
    dependencies=['H1-H3', 'Divisor-bound-elementary', 'GC-weighted-square-root-exact-resonance-mass',
                  'GC-complete-distinct-radical-twelfth-reduction'],
    implies=[], blockers=[],
    evidence=dict(positive=[kernel.as_posix(), *[p.as_posix() for p in evidence], judge.as_posix()], negative=[], inconclusive=[]),
    owner='Codex conductor',
    next_action='Keep the complete signed distinct-class target open; preserve the oscillatory kernel before norms and require a fully paid joint signed estimate. Track an explicitly sufficient unbounded-fixed-order family.',
)
patch = dict(
    round_index=217, campaign_id=cid, starting_graph_sha256=start[gp.as_posix()],
    proof_obligations=dict(create=[node], update=[], correct_rejected=[], reject=[], no_change=protected),
    round_assessment=dict(terminal_label=decision['terminal_label'], reason=decision['reason']),
    reversibility=dict(remove_created_ids=[node_id], rule='Remove the sole created node to restore all previous graph data and original graph bytes; replay differs only in a normalized creation timestamp.'),
)
assert not validate_patch_against_graph(g, patch)
applied, result = apply_state_patch(copy.deepcopy(g), patch, round_index=217, judge_ref=judge.as_posix())
assert result.created == [node_id] and not result.updated and not result.rejected and not result.corrected_rejected
assert applied['proof_obligations'][:-1] == g['proof_obligations']
assert all(applied[k] == g[k] for k in g if k != 'proof_obligations')
assert not validate_graph(applied, root=root)
idx = {n['id']: n for n in applied['proof_obligations']}
done = set()


def walk(i, active):
    assert i in idx and i not in active
    if i in done:
        return
    assert idx[i]['status'] in ['proved_internal', 'proved_external_dependency'], i
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
replay, _ = apply_state_patch(copy.deepcopy(restored), patch, round_index=217, judge_ref=judge.as_posix())
replay['proof_obligations'][-1]['last_updated_at'] = applied['proof_obligations'][-1]['last_updated_at']
assert replay == applied
write(base / 'state_patch.json', patch)
preflight = dict(round_index=217, status='green_create_only_obstruction_preflight',
    graph_schema='pass', campaign_schema='pass', state_patch='pass',
    all_400_existing_nodes_and_other_graph_data_unchanged=True,
    dependency_cone='acyclic_and_all_accepted', dependency_cone_nodes=sorted(done),
    reverse_to_original_graph_bytes='pass', replay='pass', frozen_scope='pass',
    protected_archive_entries_checked=archive_count, numerical_experiments=0,
    analytical_algebraic_percent_at_least=95, complete_moment_bound_improved=False,
    pointwise_exponent_change=False)
write(base / 'controls/promotion_preflight.json', preflight)
matrix = read('state/validation_matrix.yml')
oldgates = copy.deepcopy([x for x in matrix['gates'] if not x['id'].startswith('round217_')])
for gate in matrix['gates']:
    if gate['id'].startswith('round217_'):
        gate['status'] = 'green_narrow_obstruction_only_signed_target_open'
for p in all_reviews:
    matrix['gates'].append(dict(id='round217_' + p.stem, status='green', artifact=p.as_posix()))
matrix['gates'].append(dict(id='round217_patch_reverse_replay', status='green', artifact=(base / 'controls/promotion_preflight.json').as_posix()))
round_gates = [x for x in matrix['gates'] if x['id'].startswith('round217_')]
assert len(round_gates) == 11 and all(x['status'].startswith('green') and Path(x['artifact']).is_file() for x in round_gates)
assert oldgates == [x for x in matrix['gates'] if not x['id'].startswith('round217_')]
matrix['promotion_status'] = 'round_217_gates_green_narrow_obstruction_ready_to_apply'
write('state/validation_matrix.yml', matrix)

# All required gates precede the first mathematical-state mutation.
assert gp.read_bytes() == oldraw and draft.read_bytes() == old_draft
assert all(sha(p) == h for p, h in start.items())
write_graph(gp, applied)
assert load_graph(gp) == applied
finalhash = sha(gp)
matrix.update(promotion_status='round_217_closed_narrow_obstruction_only', graph_sha256=finalhash,
    analytic_target_status='open_complete_signed_distinct_class_integral',
    decision_rule='One absolute-certificate obstruction accepted; all400 prior nodes and every complete moment/pointwise power unchanged. Full-goal strategy review complete; next broad review220.')
write('state/validation_matrix.yml', matrix)
addition = '''
## Round217 accepted distinct-class absolute-certificate obstruction

The accepted node `GC-distinct-radical-absolute-certificate-obstruction`
shows that taking termwise Fourier moduli still fails after restricting
all squarefree classes to be distinct and greater than Q=floor(T^alpha).
For each fixed even p>=4 and fixed alpha<1, one actual positive block
n comparable to T and one balanced sign pattern have certificate at least
c T^(p/4-1/2). Weighted root-sum bins supply close tuples; a same-block
class-energy bound and a last-index count remove every repeated class
with a smaller error. Actual coefficients and real endpoints are retained.

At p=12,alpha=2/5 this is T^(5/2), exceeding the target T^(29/25).
This is only a lower bound on the named termwise absolute certificate.
It does not lower-bound signed I12 or any physical moment, and it does
not disprove the target. All previous accepted powers and parent statuses
are unchanged. The complete signed estimate and quarter theorem remain
open. See `proofs/kernels/gc_distinct_radical_absolute_certificate_obstruction.md`.
The conditional moment-family analysis is strategy evidence, not an
accepted new moment bound.
'''
assert b'## Round217 accepted distinct-class absolute-certificate obstruction' not in old_draft
put(draft, old_draft + addition.encode())
assert draft.read_bytes().startswith(old_draft)
assessment = dict(decision=decision['decision'], terminal_label=decision['terminal_label'], graph_mutation=True,
    main_result=decision['reason'], resulting_graph_sha256=finalhash,
    patch_effect=f'1_create_0_update_0_correct_0_reject_{len(protected)}_no_change',
    complete_moment_bound_improved=False, pointwise_exponent_change=False,
    goal_turn_classification=decision['goal_turn_classification'])
m.update(status='complete', completed_at=now, closing_assessment=assessment,
    post_report_reviews=[p.as_posix() for p in all_reviews], conductor_interventions=decision['interventions'])
for t in m['tasks']:
    t['status'] = 'completed'
assert not validate_campaign(m, applied, root=root)
write('state/active_campaign.yml', m)
lp = Path('state/round_ledger.yml')
ledger_raw = lp.read_bytes()
s = ledger_raw.decode()
ledger = json.loads(s)
assert ledger['active_round'] == 217 and ledger['rounds'][-1]['round_index'] == 217
oldentries = copy.deepcopy(ledger['rounds'][:-1])
entry = ledger['rounds'][-1]
entry.update(status='closed', closing_assessment=assessment, completed_at=now, next_round=218)
for t in entry['tasks']:
    t['status'] = 'completed'
matches = list(re.finditer(r'    \{\r?\n      "round_index": 217,', s))
assert len(matches) == 1
pos = matches[0].start()
eol = '\r\n' if '\r\n' in s else '\n'
new = s[:pos] + eol.join('    ' + line for line in json.dumps(entry, indent=2, ensure_ascii=False).splitlines()) + eol + '  ]' + eol + '}' + eol
assert json.loads(new) == ledger and ledger['rounds'][:-1] == oldentries
assert new[:pos].encode() == ledger_raw[:len(s[:pos].encode())]
put(lp, new.encode())

# Record only a pending successor after closure, not a new frozen round.
write('state/next_round_plan.yml', dict(round_index=218, status='pending_design', campaign_id=None, tasks=[],
    starting_graph_sha256=finalhash, predecessor_round=217, predecessor_terminal_label=decision['terminal_label'],
    candidate_objective=decision['next_objective'], candidate_method=decision['next_method'],
    first_unproved_estimate=decision['first_unproved_estimate'],
    exact_closed_dependencies=[kernel.as_posix(), checkpoint.as_posix(), (base / 'synthesis.md').as_posix(), judge.as_posix(), *[p.as_posix() for p in evidence]],
    design_constraint='One complete actual signed estimate, with every remainder paid; preserve kernel phases before norms. No repeat of positive spacing, free centering, scalar Poisson or absolute CRT without a new complete signed bound.',
    full_goal_scope='Quarter remains the target; track Q_p=T^(1/p), I_p<=T^(5/4+epsilon) along unbounded fixed even orders as sufficient unproved premises.',
    scheduled_review='Next mandatory broad strategy/current-primary-literature review220 after217--219.',
    prior_turn_classification=decision['goal_turn_classification']))
summary = _next_campaign(m, output_dir=base, graph_hash=finalhash)
summary += '\n## Closing decision\n\nRound217 closed with one narrow distinct-class absolute-certificate obstruction. All400 previous nodes and complete powers unchanged. The conditional family grants, signed I12 and quarter theorem remain open. Next218 pending design; broad review220.\n'
for p in ['state/current_round.md', 'state/next_campaign.md']:
    put(p, summary.encode())
note = '\n## Round217 full-goal distinct-source review (2026-09-28)\n\n' + decision['state_note'] + '\n'
for p in ['state/project_summary.md', 'state/current_state.md', 'state/failure_ledger.md']:
    raw = Path(p).read_bytes()
    assert b'## Round217 full-goal distinct-source review' not in raw
    put(p, raw + note.encode())
assert sha('strategy/gauss_circle_strategy_review_2026-09-23.md') == start['strategy/gauss_circle_strategy_review_2026-09-23.md']
validation = dict(preflight, status='green_round217_distinct_absolute_certificate_obstruction_only',
    campaign_id=cid, generated_at=now, terminal_label=decision['terminal_label'],
    starting_graph_sha256=start[gp.as_posix()], starting_canonical_sha256=oldcanon,
    final_graph_sha256=finalhash, graph_nodes=401, new_nodes=[node_id],
    proof_draft_appended_only_after_valid_graph=True, old_proof_draft_bytes_preserved=True,
    final_proof_draft_sha256=sha(draft), previous_ledger_prefix_bytes_unchanged=True,
    legacy_paths_unchanged=True, next_strategy_checkpoint=220, green_round_gates=len(round_gates))
write(base / 'controls/closure_validation.json', validation)
vtext = f'''# Round217 closure validation

GREEN for the narrow distinct-class absolute-certificate obstruction only.
One new internal lemma; all400 previous nodes and other graph data unchanged.
The complete signed target, moment-family grants and quarter theorem remain
OPEN. Final graph SHA256:{finalhash}. Three frozen reports, two statement-only
derivations and final-hash source/mathematical seams pass. Reverse restored
the original graph bytes; replay and accepted acyclic dependency cone pass.
All11 required gates were green before application; proof draft appended
afterward, with its old bytes preserved. All402 prior archive entries,
frozen scope, prior ledger prefix and legacy paths are unchanged. Zero
mathematical numerical experiments. No global historical recertification.
Next218 is pending design; next mandatory broad review220.
Details:{base.as_posix()}/controls/closure_validation.json.
'''
for p in ['state/last_validation.md', 'state/last_validation_report.md']:
    put(p, vtext.encode())
assert not validate_graph(load_graph(gp), root=root)
assert not validate_campaign(read('state/active_campaign.yml'), applied, root=root)
assert not subprocess.check_output(['git', 'diff', '--name-only', '--', 'rounds/obligation-main', 'rounds/web-research-test']).strip()
subprocess.run(['git', 'diff', '--check'], check=True)
hashes = {p.relative_to(root).as_posix(): sha(p) for p in sorted((root / base).rglob('*'))
          if p.is_file() and p.name != 'artifact_hashes.json' and '__pycache__' not in p.parts}
for p in [kernel, checkpoint, Path('strategy/round217_full_goal_distinct_source_review.md')]:
    hashes[p.as_posix()] = sha(p)
write(base / 'controls/artifact_hashes.json', hashes)
print(json.dumps({k: validation[k] for k in ['status', 'graph_nodes', 'new_nodes', 'final_graph_sha256',
    'green_round_gates', 'protected_archive_entries_checked', 'complete_moment_bound_improved', 'pointwise_exponent_change']}, indent=2))
