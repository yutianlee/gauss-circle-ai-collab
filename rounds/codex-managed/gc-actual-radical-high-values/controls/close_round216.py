"""Close round216 and accept only its fully reviewed complete reduction."""
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

cid = 'gc-actual-radical-high-values'
base = Path('rounds/codex-managed') / cid
gp = Path('state/proof_obligations.yml')
draft = Path('state/best_proof_draft.md')
candidate = base / 'candidates/complete_distinct_radical_reduction.md'
kernel = Path('proofs/kernels/gc_complete_distinct_radical_moment_reduction.md')
power = base / 'controls/conductor_radical_ledger.md'
node_id = 'GC-complete-distinct-radical-twelfth-reduction'
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
priors = [
    'm9-m1-t1-complete-source-coefficient-mask-analysis',
    'gc-whole-discrepancy-twelfth-moment',
    'gc-strategy-signed-moment-majorant-review',
    'gc-complete-signed-convolution-attack',
    'gc-complete-large-values-duality',
    'gc-full-frontier-moment-strategy-review',
    'gc-complete-signed-shell-arithmetic',
    'gc-signed-rational-filter-attack',
    'gc-full-proof-signed-arithmetic-review',
    'gc-complete-signed-tenth-moment',
    'gc-signed-near-frequency-cancellation',
    'gc-full-source-method-review',
    'gc-complete-four-point-correlation',
    'gc-complete-centered-arithmetic',
    'gc-full-goal-radius-source-review',
    'gc-complete-localized-wave-moment',
]
archive_count = 0
for prior in priors:
    for p, h in read(Path('rounds/codex-managed') / prior / 'controls/artifact_hashes.json').items():
        assert sha(p) == h, ('archive', p)
        archive_count += 1
assert archive_count == 373, archive_count

oldraw = gp.read_bytes()
old_draft = draft.read_bytes()
g = load_graph(gp)
oldcanon = hashlib.sha256(dump_graph(g).encode()).hexdigest()
assert len(g['proof_obligations']) == 399 and not validate_graph(g, root=root)
m = read('state/active_campaign.yml')
assert m['round_index'] == 216 and m['campaign_id'] == cid and m['status'] == 'active'
assert not validate_campaign(m, g, root=root)
frozen = read(base / 'plan.json')['campaign']
for key in ['frozen_target', 'completion_criteria', 'resource_policy', 'controls', 'target_obligations', 'review_seams']:
    assert m[key] == frozen[key], key
assert len(m['tasks']) == len(frozen['tasks']) == 3
for task, original in zip(m['tasks'], frozen['tasks']):
    assert {k: v for k, v in task.items() if k != 'status'} == {k: v for k, v in original.items() if k != 'status'}
    contract(task['report_path'])

fixed = {
    'reports/actual_radical_tail.md': 'f8c6ff6b2ecd0f5b5458d63856d4615967d7442fe693e39c9633c5b61b56a954',
    'reports/anchored_divisor_high_values.md': '7fb1a536ef78d6e2af007bf179fa8c3ce74cda69c96948a81043b3a4cf9213d8',
    'reports/blind_radical_cutoff.md': 'e0accd624e0d9f1b95644c3456ed6302f9ac145aa6d4356aba4fb6cf82c7595e',
    'candidates/complete_distinct_radical_reduction.md': 'd7a5945f834c565c11cdc26bc3480de12d173e35de28c734381392f5feecb1ee',
    'controls/conductor_radical_ledger.md': '5d7e3daaecfb20771d5a4adc79cf07717d0805a32f2a29ca673671af3a550f72',
    'reviews/independent_distinct_reduction_review.md': '1d786fbd52cef98d9bb05c6f26632b3d753fa8daf012695c5619a18e987e37ee',
    'reviews/independent_radical_report_review.md': '5059b747af33bc0da45c424539d713d2006e8e9585eed5112e87e975d736b9b1',
    'reviews/independent_anchored_arithmetic_review.md': 'd1e2c08aa2c04f38825e1cd0b77b3ef67b4fe23f60d5d20b6daeb6d2be404c41',
    'reviews/isolated_distinct_class_rederivation.md': 'd5317e2a40bb394bd5eca45d57d1ebfe0d4c636fcf6a9b4a17e6f8314efc2256',
    'reviews/independent_actual_radical_binding_review.md': '12b0118251e530e516612c1223d3d5f047ce1ff4603a2cececa6661f8be1785d',
}
for rel, h in fixed.items():
    assert sha(base / rel) == h, ('final frozen artifact', rel)
contract(candidate)
contract(power)
isolated = base / 'reviews/isolated_distinct_class_rederivation.md'
packet = base / 'briefs/isolated_distinct_class_statement.md'
assert packet.is_file()
assert 'No claimant, ledger, graph, manifest, strategy' in contract(isolated)
reviews = [
    (base / 'reviews/conductor_blind_radical_review.md', [base / 'reports/blind_radical_cutoff.md']),
    (base / 'reviews/independent_distinct_reduction_review.md', [candidate]),
    (base / 'reviews/independent_radical_report_review.md', [base / 'reports/actual_radical_tail.md']),
    (base / 'reviews/independent_anchored_arithmetic_review.md', [base / 'reports/anchored_divisor_high_values.md']),
    (base / 'reviews/independent_actual_radical_binding_review.md', [candidate, power]),
]
for p, artifacts in reviews:
    s = contract(p)
    assert 'GREEN' in s, p
    for a in artifacts:
        assert sha(a) in s.lower(), ('review binding', p, a)
all_reviews = [p for p, _ in reviews] + [isolated]
decision = read(base / 'controls/closing_decision.json')
assert decision['graph_mutation'] is True
assert decision['complete_moment_bound_improved'] is False and decision['pointwise_exponent_change'] is False
contract(base / 'synthesis.md')
evidence = [Path(t['report_path']) for t in m['tasks']] + [candidate, power, packet] + all_reviews
judge = base / 'reviews/conductor_round216_reconciliation.md'
s = contract(judge)
bindings = '\n'.join(f'- `{p.as_posix()}`: `{sha(p)}`.' for p in evidence)
if 'FINAL_HASH_BINDINGS' in s:
    put(judge, s.replace('FINAL_HASH_BINDINGS', bindings).encode())
else:
    assert bindings in s
assert 'GREEN for the complete distinct-radical reduction only' in contract(judge)

# The accepted proof is byte-for-byte the independently reviewed candidate.
if kernel.exists():
    assert kernel.read_bytes() == candidate.read_bytes()
else:
    put(kernel, candidate.read_bytes())
assert sha(kernel) == fixed['candidates/complete_distinct_radical_reduction.md']
hygiene = []
for p in [kernel, *base.rglob('*.md')]:
    raw = p.read_bytes()
    s = raw.decode('utf-8')
    assert not re.search(rb'\r(?!\n)', raw), p
    assert '\ufffd' not in s and not any(ord(c) < 32 and c not in '\n\r\t' for c in s), p
    hygiene.append(p.as_posix())
assert not subprocess.check_output(['git', 'diff', '--name-only', '--', 'rounds/obligation-main', 'rounds/web-research-test']).strip()
subprocess.run(['git', 'diff', '--check'], check=True)

protected = [
    'GC-target', 'Conditional-bridge', 'M9', 'M9-M1', 'M9-M2', 'M9-endpoint-uniformity',
    'GC-external-Li-Yang-theta-star', 'GC-weighted-square-root-exact-resonance-mass',
    'GC-physical-twelfth-moment-absolute-majorant-obstruction',
    'GC-complete-square-root-large-values-moment-bound',
]
assert node_id not in {n['id'] for n in g['proof_obligations']}
node = dict(
    id=node_id, type='lemma', track='proof_infrastructure', status='proved_internal',
    title='Complete actual twelfth-moment reduction to distinct large squarefree classes',
    statement_tex=(
        'Fix a nonnegative real radial smooth unit-mass mollifier supported in the unit disk, '
        'Psi(s)=rho-hat(s e1), and a fixed nonnegative smooth w supported in [1/2,2] '
        'and equal1 on [1/sqrt(2),sqrt(3)]. For real T>=2 let '
        'a_n(T)=r2(n)n^(-3/4)Psi(sqrt(n/T)), '
        'f_d(R)=sum_(s>=1)a_(d s^2)(T)cos(2pi R s sqrt(d)-3pi/4), '
        'Q=floor(T^(2/5)), L_Q=sum_(squarefree d<=Q)f_d, Z_Q=sum_(squarefree d>Q)f_d, '
        'B_T=L_Q+Z_Q, E12=sum_(ordered pairwise distinct squarefree d_1,...,d_12>Q)product_j f_(d_j), '
        'I12=integral w(R/T)E12(R)dR and M_p(F)=integral w(R/T)|F|^p dR. '
        'With the existing qualified Li--Yang exponent theta_LY and beta=2theta_LY-1/2, '
        'M12(L_Q)<<_epsilon T^(15/13+epsilon) and '
        'integral w(R/T)|Z_Q^12-E12|dR<<_epsilon T^(8beta-1/5+epsilon). '
        'Consequently |M12(Z_Q)-I12| obeys the latter error bound. '
        'The complete high-value bound integral_(|B_T|>T^(13/125))w|B_T|^12<<T^(29/25+epsilon), '
        'the full B_T twelfth-moment bound at that power, the full Z_Q bound at that power, '
        'and |I12|<<T^(29/25+epsilon) are equivalent, with every bound quantified for each epsilon>0. '
        'A one-sided upper bound on real I12 suffices. None of these equivalent target bounds is proved here. '
        'The exact signed partition identity pays every repeated-class configuration collectively, '
        'including nonzero and nonpairing relations, with all harmonics, signs, blocks, tails, real endpoints '
        'and floor retained. Distinct-class frequencies are nonzero but no sufficient separation or '
        'cancellation estimate is proved. This is not an additive approximation to M12(B_T), '
        'a new complete moment or pointwise exponent, a sufficient unbounded-order family, '
        'or a proof of any M1/M2/GAR parent, endpoint or the quarter theorem.'
    ),
    dependencies=[
        'H1-H3', 'Divisor-bound-elementary',
        'GC-complete-square-root-large-values-moment-bound',
        'GC-weighted-square-root-exact-resonance-mass', 'GC-external-Li-Yang-theta-star',
    ],
    implies=[], blockers=[],
    evidence=dict(positive=[kernel.as_posix(), *[p.as_posix() for p in evidence], judge.as_posix()], negative=[], inconclusive=[]),
    owner='Codex conductor',
    next_action='At mandatory broad strategy/current-literature review217 compare the complete remaining distinct-class signed integral and anchored energy with all full-proof frontiers. The 29/25 target and full quarter theorem remain open; preserve every inherited source qualification.',
)
patch = dict(
    round_index=216, campaign_id=cid, starting_graph_sha256=start[gp.as_posix()],
    proof_obligations=dict(create=[node], update=[], correct_rejected=[], reject=[], no_change=protected),
    round_assessment=dict(terminal_label=decision['terminal_label'], reason=decision['reason']),
    reversibility=dict(remove_created_ids=[node_id], rule='Remove the sole created node to restore every previous graph entry and the original graph bytes. Replay is identical after normalizing only the new-node timestamp.'),
)
assert not validate_patch_against_graph(g, patch)
applied, result = apply_state_patch(copy.deepcopy(g), patch, round_index=216, judge_ref=judge.as_posix())
assert result.created == [node_id] and not result.updated and not result.rejected and not result.corrected_rejected
assert applied['proof_obligations'][:-1] == g['proof_obligations']
assert all(applied[k] == g[k] for k in g if k != 'proof_obligations')
assert not validate_graph(applied, root=root)
idx = {n['id']: n for n in applied['proof_obligations']}
done = set()


def walk(i, active):
    assert i in idx and i not in active, ('dependency cycle or missing node', i)
    if i in done:
        return
    assert idx[i]['status'] in ['proved_internal', 'proved_external_dependency'], ('unaccepted dependency', i)
    active.add(i)
    for dependency in idx[i].get('dependencies', []):
        walk(dependency, active)
    active.remove(i)
    done.add(i)


walk(node_id, set())
assert all(Path(p).is_file() for p in node['evidence']['positive'])
restored = copy.deepcopy(applied)
restored['proof_obligations'] = [n for n in restored['proof_obligations'] if n['id'] != node_id]
assert restored == g and hashlib.sha256(dump_graph(restored).encode()).hexdigest() == oldcanon
newline = '\r\n' if b'\r\n' in oldraw else '\n'
assert dump_graph(restored).replace('\n', newline).encode() == oldraw
replay, _ = apply_state_patch(copy.deepcopy(restored), patch, round_index=216, judge_ref=judge.as_posix())
replay['proof_obligations'][-1]['last_updated_at'] = applied['proof_obligations'][-1]['last_updated_at']
assert replay == applied
write(base / 'state_patch.json', patch)
preflight = dict(
    round_index=216, status='green_create_only_reduction_patch_preflight',
    graph_schema='pass', campaign_schema='pass', state_patch='pass',
    all_399_existing_nodes_and_other_graph_data_unchanged=True,
    dependency_cone='acyclic_and_all_accepted', dependency_cone_ids=sorted(done),
    reverse_original_graph_bytes='pass', replay_except_new_timestamp='pass',
    exact_review_bindings={a.as_posix(): sha(a) for _, artifacts in reviews for a in artifacts},
    final_review_hashes={p.as_posix(): sha(p) for p in all_reviews},
    isolated_packet_sha256=sha(packet), candidate_and_kernel_sha256=sha(kernel),
    frozen_scope_and_briefs_unchanged=True, original_reports_unchanged=True,
    closed_round200_through215_archives_unchanged=True, protected_archive_entries_checked=archive_count,
    report_hygiene=hygiene, mathematical_numerical_experiments=0,
    analytic_target='open_complete_signed_distinct_class_integral',
    complete_moment_bound_improved=False, pointwise_exponent_change=False,
    validation_scope='New reduction and accepted dependency cone only; no global recertification of historical mathematics or inherited advisories.',
)
write(base / 'controls/promotion_preflight.json', preflight)
matrix = read('state/validation_matrix.yml')
oldgates = copy.deepcopy([x for x in matrix['gates'] if not x['id'].startswith('round216_')])
assert len([x for x in matrix['gates'] if x['id'].startswith('round216_')]) == 4
for gate in matrix['gates']:
    if gate['id'].startswith('round216_'):
        gate['status'] = 'green_complete_reduction_only_target_open'
for p in all_reviews:
    matrix['gates'].append(dict(id='round216_' + p.stem, status='green', artifact=p.as_posix()))
matrix['gates'].append(dict(id='round216_patch_reverse_replay', status='green', artifact=(base / 'controls/promotion_preflight.json').as_posix()))
round_gates = [x for x in matrix['gates'] if x['id'].startswith('round216_')]
assert len(round_gates) == 11 and all(x['status'].startswith('green') and Path(x['artifact']).is_file() for x in round_gates)
assert oldgates == [x for x in matrix['gates'] if not x['id'].startswith('round216_')]
matrix['promotion_status'] = 'round_216_gates_green_complete_reduction_ready_to_apply'
write('state/validation_matrix.yml', matrix)

# First mathematical-state mutation: every required gate has passed.
assert gp.read_bytes() == oldraw and draft.read_bytes() == old_draft
assert all(sha(p) == h for p, h in start.items())
write_graph(gp, applied)
assert load_graph(gp) == applied
finalhash = sha(gp)
matrix.update(
    promotion_status='round_216_closed_complete_distinct_radical_reduction_only',
    graph_sha256=finalhash, analytic_target_status='open_complete_signed_distinct_class_integral',
    decision_rule='One complete arithmetic reduction accepted; all399 previous nodes and all complete moment/pointwise powers unchanged. Mandatory broad strategy/current-literature review217 is next.',
)
write('state/validation_matrix.yml', matrix)
addition = '''
## Round216 accepted complete distinct-radical reduction

The accepted node `GC-complete-distinct-radical-twelfth-reduction`
uses the actual full mollified cosine series and Q=floor(T^(2/5)).
The small-squarefree-class head satisfies M12(L_Q)<<T^(15/13+epsilon).
For the tail Z_Q and the ordered twelve-distinct-class product sum E12,
the complete collective error is
integral w(R/T)|Z_Q^12-E12|dR<<T^(8beta-1/5+epsilon),
where beta=2theta_LY-1/2 and 8beta-1/5<21/25. The exact partition
identity includes every repeated-class configuration, including nonzero
and nonpairing relations, with all infinite harmonics and signs retained.

The high-value gate at V0=T^(13/125), the full B_T and Z_Q twelfth
moment bounds at T^(29/25+epsilon), and the bound on the absolute value
of I12=integral w(R/T)E12 are equivalent. A one-sided upper bound on
real I12 suffices. None of these equivalent target bounds is proved.
The small additive error is for M12(Z_Q); the B_T-to-Z_Q transfer uses
the paid head and power inequalities and is not an additive approximation.

The remaining actual displaced Fourier kernel over twelve distinct
large squarefree classes is unestimated. This supplies a complete
reduction but no improved complete moment or pointwise exponent.
Even the open target would give only102/325, not the quarter theorem.
No sufficient unbounded-order family or M1/M2/GAR parent is proved.
See `proofs/kernels/gc_complete_distinct_radical_moment_reduction.md`.
'''
assert b'## Round216 accepted complete distinct-radical reduction' not in old_draft
put(draft, old_draft + addition.encode())
assert draft.read_bytes().startswith(old_draft)
assessment = dict(
    decision=decision['decision'], terminal_label=decision['terminal_label'], graph_mutation=True,
    main_result=decision['reason'], resulting_graph_sha256=finalhash,
    patch_effect=f'1_create_0_update_0_correct_0_reject_{len(protected)}_no_change',
    complete_moment_bound_improved=False, pointwise_exponent_change=False,
    goal_turn_classification=decision['goal_turn_classification'],
)
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
assert ledger['active_round'] == 216 and ledger['rounds'][-1]['round_index'] == 216
oldentries = copy.deepcopy(ledger['rounds'][:-1])
entry = ledger['rounds'][-1]
entry.update(status='closed', closing_assessment=assessment, completed_at=now, next_round=217)
for t in entry['tasks']:
    t['status'] = 'completed'
matches = list(re.finditer(r'    \{\r?\n      "round_index": 216,', s))
assert len(matches) == 1
pos = matches[0].start()
eol = '\r\n' if '\r\n' in s else '\n'
new = s[:pos] + eol.join('    ' + line for line in json.dumps(entry, indent=2, ensure_ascii=False).splitlines()) + eol + '  ]' + eol + '}' + eol
assert json.loads(new) == ledger and ledger['rounds'][:-1] == oldentries
assert new[:pos].encode() == ledger_raw[:len(s[:pos].encode())]
put(lp, new.encode())

# Successor design remains pending, and is identified only after recorded closure.
write('state/next_round_plan.yml', dict(
    round_index=217, status='pending_design', campaign_id=None, tasks=[],
    starting_graph_sha256=finalhash, predecessor_round=216,
    predecessor_terminal_label=decision['terminal_label'],
    candidate_objective=decision['next_objective'], candidate_method=decision['next_method'],
    first_unproved_estimate=decision['first_unproved_estimate'],
    exact_closed_dependencies=[kernel.as_posix(), (base / 'synthesis.md').as_posix(), judge.as_posix(),
        *[p.as_posix() for p in evidence], 'strategy/gauss_circle_strategy_checkpoint_round214_2026-09-28.md'],
    design_constraint='Mandatory broad full-goal and current-primary-literature review before selecting another analytic mechanism. Assess every complete proof frontier; no routine repeat of termwise absolute certificates or generic exact-to-finite-time independence.',
    full_goal_scope='P(X)<<X^(1/4+epsilon) remains open. The fixed twelfth target would give102/325 only. Seek a complete sufficient unbounded-fixed-order family or complete alternative parents.',
    scheduled_review='Round217 mandatory after214--216; review current primary literature as of execution date.',
    prior_turn_classification=decision['goal_turn_classification'],
))
summary = _next_campaign(m, output_dir=base, graph_hash=finalhash)
summary += '\n## Closing decision\n\nRound216 closed with one accepted complete distinct-radical reduction. All399 prior nodes and all complete moment/pointwise powers are unchanged. The remaining signed target and full quarter theorem are open. Mandatory broad strategy/current-literature review217 is pending design.\n'
for p in ['state/current_round.md', 'state/next_campaign.md']:
    put(p, summary.encode())
note = '\n## Round216 complete distinct-radical reduction (2026-09-28)\n\n' + decision['state_note'] + '\n'
for p in ['state/project_summary.md', 'state/current_state.md', 'state/failure_ledger.md']:
    raw = Path(p).read_bytes()
    assert b'## Round216 complete distinct-radical reduction' not in raw
    put(p, raw + note.encode())
assert sha('strategy/gauss_circle_strategy_review_2026-09-23.md') == start['strategy/gauss_circle_strategy_review_2026-09-23.md']
assert not subprocess.check_output(['git', 'diff', '--name-only', '--', 'rounds/obligation-main', 'rounds/web-research-test']).strip()
validation = dict(
    preflight, status='green_round216_complete_distinct_radical_reduction_only',
    campaign_id=cid, generated_at=now, terminal_label=decision['terminal_label'],
    starting_graph_sha256=start[gp.as_posix()], starting_canonical_sha256=oldcanon,
    final_graph_sha256=finalhash, graph_nodes=400, new_nodes=[node_id],
    proof_draft_appended_only_after_valid_graph=True, old_proof_draft_bytes_preserved=True,
    final_proof_draft_sha256=sha(draft), previous_ledger_prefix_bytes_unchanged=True,
    legacy_paths_unchanged=True, next_strategy_checkpoint=217, green_round_gates=len(round_gates),
)
write(base / 'controls/closure_validation.json', validation)
vtext = f'''# Round216 closure validation

GREEN for the complete distinct-radical reduction only. The complete signed
target, H216, pointwise improvement and full quarter theorem remain OPEN.
One new internal lemma; all399 prior nodes and other graph data unchanged.
Final graph SHA256:{finalhash}. Three frozen reports, two isolated
derivations, final-hash seams and conductor reconciliation pass. The patch
was reversed to the original graph bytes and replayed. Its accepted
dependency cone and11 required green gates were checked before application.
The proof draft was appended afterward with old bytes preserved. All373
prior archive entries, frozen scope and briefs, prior ledger prefix and
legacy paths are unchanged. No mathematical numerical experiment. These
checks do not globally recertify historical mathematics. Mandatory broad
strategy/current-literature review217 is pending design.
Details:{base.as_posix()}/controls/closure_validation.json.
'''
for p in ['state/last_validation.md', 'state/last_validation_report.md']:
    put(p, vtext.encode())
assert not validate_graph(load_graph(gp), root=root)
assert not validate_campaign(read('state/active_campaign.yml'), applied, root=root)
subprocess.run(['git', 'diff', '--check'], check=True)
hashes = {p.relative_to(root).as_posix(): sha(p) for p in sorted((root / base).rglob('*'))
          if p.is_file() and p.name != 'artifact_hashes.json' and '__pycache__' not in p.parts}
strategy = Path('strategy/round216_actual_radical_high_values.md')
hashes.update({kernel.as_posix(): sha(kernel), strategy.as_posix(): sha(strategy)})
write(base / 'controls/artifact_hashes.json', hashes)
print(json.dumps({k: validation[k] for k in [
    'status', 'graph_nodes', 'new_nodes', 'final_graph_sha256', 'green_round_gates',
    'protected_archive_entries_checked', 'complete_moment_bound_improved', 'pointwise_exponent_change',
]}, indent=2))
