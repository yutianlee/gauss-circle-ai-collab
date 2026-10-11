"""Close Round207 only after exact-hash reviews; preserve mathematical state."""
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
    load_graph, dump_graph, validate_graph,
    validate_patch_against_graph, apply_state_patch,
)

cid = 'gc-signed-rational-filter-attack'
base = Path('rounds/codex-managed') / cid
now = datetime.now(timezone.utc).isoformat()
terminal = 'scoped_rational_method_no_go'
gp = Path('state/proof_obligations.yml')

def read(p):
    return json.loads(Path(p).read_text(encoding='utf-8-sig'))

def write(p, obj):
    Path(p).write_text(json.dumps(obj, indent=2, ensure_ascii=False) + '\n',
                       encoding='utf-8', newline='\n')

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def contract(p):
    s = Path(p).read_text(encoding='utf-8')
    assert all(re.search(rf'^#{{1,2}} {i}\.', s, re.M) for i in range(1, 8)), p
    return s

start = read(base / 'controls/starting_state_hashes.json')
assert all(sha(p) == h for p, h in start.items()), 'Protected starting state changed'
for p, h in read(base / 'controls/frozen_artifact_hashes.json').items():
    assert sha(p) == h, ('Frozen input changed', p)
prior_campaigns = [
    'm9-m1-t1-complete-source-coefficient-mask-analysis',
    'gc-whole-discrepancy-twelfth-moment',
    'gc-strategy-signed-moment-majorant-review',
    'gc-complete-signed-convolution-attack',
    'gc-complete-large-values-duality',
    'gc-full-frontier-moment-strategy-review',
    'gc-complete-signed-shell-arithmetic',
]
archive_count = 0
for prior in prior_campaigns:
    for p, h in read(Path('rounds/codex-managed') / prior / 'controls/artifact_hashes.json').items():
        assert sha(p) == h, ('Closed artifact changed', p)
        archive_count += 1

oldraw = gp.read_bytes()
g = load_graph(gp)
assert len(g['proof_obligations']) == 399 and not validate_graph(g, root=root)
m = read('state/active_campaign.yml')
assert m['round_index'] == 207 and m['campaign_id'] == cid and m['status'] == 'active'
assert not validate_campaign(m, g, root=root)
frozen = read(base / 'plan.json')['campaign']
for key in ['frozen_target', 'completion_criteria', 'resource_policy', 'controls',
            'target_obligations', 'review_seams']:
    assert m[key] == frozen[key], ('Frozen scope drift', key)
assert len(m['tasks']) == len(frozen['tasks']) == 3
for t, f in zip(m['tasks'], frozen['tasks']):
    assert {k: v for k, v in t.items() if k != 'status'} == {
        k: v for k, v in f.items() if k != 'status'}
    contract(t['report_path'])

power = base / 'controls/conductor_rational_norm_ledger.md'
contract(power)
reviews = [
    (base / 'reviews/independent_signed_norm_review.md',
     [base / 'reports/periodic_hyperbola_attack.md', power]),
    (base / 'reviews/independent_rational_majorant_review.md',
     [base / 'reports/signed_rational_moment_attack.md']),
    (base / 'reviews/independent_threshold_even_cutoff_review.md',
     [base / 'reports/blind_periodic_threshold.md', power]),
]
for review, artifacts in reviews:
    s = contract(review)
    assert 'GREEN' in s, review
    for artifact in artifacts:
        assert sha(artifact).lower() in s.lower(), (review, artifact)

evidence = [Path(t['report_path']) for t in m['tasks']] + [power]
evidence += [p for p, _ in reviews]
bindings = '\n'.join(f'- `{p.as_posix()}`: `{sha(p)}`.' for p in evidence)
judge = base / 'reviews/conductor_round207_reconciliation.md'
judge_text = judge.read_text(encoding='utf-8').replace('FINAL_HASH_BINDINGS', bindings)
judge.write_text(judge_text, encoding='utf-8', newline='\n')
assert 'GREEN for scoped rational-attempt closure only' in contract(judge)
for t in m['tasks']:
    assert sha(t['report_path']) in judge_text

assert (base / 'synthesis.md').is_file()

hygiene = []
for p in base.rglob('*.md'):
    raw = p.read_bytes()
    s = raw.decode('utf-8')
    assert not re.search(rb'\r(?!\n)', raw), ('Bare CR in mathematical text', p)
    assert '\ufffd' not in s and not any(ord(c) < 32 and c not in '\n\r\t' for c in s), p
    hygiene.append(p.as_posix())
protected = [
    'GC-target', 'Conditional-bridge', 'M9', 'M9-M1', 'M9-M2',
    'M9-endpoint-uniformity', 'GC-external-Li-Yang-theta-star',
    'GC-weighted-square-root-exact-resonance-mass',
    'GC-physical-twelfth-moment-absolute-majorant-obstruction',
    'GC-complete-square-root-large-values-moment-bound',
]
reason = ('Complete signed rational-filter and reciprocal estimates recover existing bounds only. '
          'The actual termwise rational sixth majorant is at least X^3H after single-frequency '
          'grouping; signed sextuple cancellation remains open. Threshold, mask and width costs '
          'are fully paid. Archive this scoped no-go without graph promotion.')
patch = dict(
    round_index=207, campaign_id=cid, starting_graph_sha256=start[gp.as_posix()],
    proof_obligations=dict(create=[], update=[], correct_rejected=[], reject=[], no_change=protected),
    round_assessment=dict(terminal_label=terminal, reason=reason),
    reversibility=dict(rule='Identity patch. In-memory application, inverse identity and replay '
                       'equal the original graph. Graph and proof-draft bytes are not rewritten.'),
)
assert not validate_patch_against_graph(g, patch)
applied, result = apply_state_patch(copy.deepcopy(g), patch, round_index=207, judge_ref=judge.as_posix())
assert applied == g and not result.created and not result.updated
assert not result.rejected and not result.corrected_rejected
inverse = copy.deepcopy(applied)
replay, _ = apply_state_patch(copy.deepcopy(inverse), patch, round_index=207, judge_ref=judge.as_posix())
assert inverse == g and replay == g and dump_graph(replay) == dump_graph(g)
write(base / 'state_patch.json', patch)
preflight = dict(
    round_index=207, status='green_identity_patch_preflight', graph_schema='pass',
    campaign_schema='pass', identity_patch='pass', reverse_identity_replay='pass',
    all_399_nodes_and_other_graph_data_unchanged=True,
    exact_review_hashes={a.as_posix(): sha(a) for _, arts in reviews for a in arts},
    three_report_hashes={t['report_path']: sha(t['report_path']) for t in m['tasks']},
    frozen_scope_and_briefs_unchanged=True, closed_round200_through206_archives_unchanged=True,
    protected_archive_entries_checked=archive_count, report_hygiene=hygiene,
    mathematical_numerical_experiments=0, analytic_target='open',
    complete_moment_bound_improved=False, pointwise_exponent_change=False,
)
write(base / 'controls/closure_preflight.json', preflight)
matrix = read('state/validation_matrix.yml')
old_gates = copy.deepcopy([x for x in matrix['gates'] if not x['id'].startswith('round207_')])
for gate in matrix['gates']:
    if gate['id'].startswith('round207_'):
        gate['status'] = 'green_scoped_attempt_only_signed_target_open'
for review, _ in reviews:
    matrix['gates'].append(dict(id='round207_' + review.stem, status='green', artifact=review.as_posix()))
matrix['gates'].append(dict(id='round207_identity_patch_scope', status='green',
                           artifact=(base / 'controls/closure_preflight.json').as_posix()))
assert all(x['status'].startswith('green') and Path(x['artifact']).is_file()
           for x in matrix['gates'] if x['id'].startswith('round207_'))
assert old_gates == [x for x in matrix['gates'] if not x['id'].startswith('round207_')]
matrix.update(
    promotion_status='round_207_closed_identity_patch_scoped_rational_no_go', graph_sha256=sha(gp),
    analytic_target_status='open_complete_signed_middle_band_moment',
    decision_rule='Round207 closes a complete signed rational attempt and actual-coefficient '
                  'majorant no-go; signed target remains open. Identity patch, no complete gain. '
                  'Round208 pending mandatory strategy/current-literature review.',
)
write('state/validation_matrix.yml', matrix)
# Durable mathematical state is untouched: the validated and gated patch is identity.
assert gp.read_bytes() == oldraw and all(sha(p) == h for p, h in start.items())
assessment = dict(
    decision='retain_graph_archive_scoped_arithmetic_no_go', terminal_label=terminal,
    graph_mutation=False, main_result=reason, resulting_graph_sha256=sha(gp),
    patch_effect=f'0_create_0_update_0_correct_0_reject_{len(protected)}_no_change',
    complete_moment_bound_improved=False, pointwise_exponent_change=False,
    goal_turn_classification='scoped_method_no_go_precise_remaining_signed_estimate_no_complete_bound_gain',
)
m.update(status='complete', completed_at=now, closing_assessment=assessment,
         post_report_reviews=[p.as_posix() for p, _ in reviews],
         conductor_interventions=[
             'Required a complete signed estimate after periodic transformation; both arms and every harmonic retained.',
             'Separated F/e(-lambda x) and K/e(+lambda x) conventions and checked exact mod4 factors.',
             'Introduced an explicit even-cutoff variant with its own exact quotient limit; obtained independent review.',
             'Proved rational variance with collision grouping, actual width and joint prefix energy, not a power-sized mask count.',
             'Routed one post-report seam cycle after all discovery reports, preserving original blind isolation.',
             'Repaired seven bare-CR TeX defects byte-preservingly before final review hashes.',
             'Kept majorant lower bound separate from signed moment and exact-deleted variants; no graph fragments promoted.',
         ])
for t in m['tasks']:
    t['status'] = 'completed'
assert not validate_campaign(m, g, root=root)
write('state/active_campaign.yml', m)

# Preserve all earlier ledger entries and the entire prefix byte-for-byte.
lp = Path('state/round_ledger.yml')
ledger_raw = lp.read_bytes()
s = ledger_raw.decode('utf-8')
ledger = json.loads(s)
assert ledger['active_round'] == 207 and ledger['rounds'][-1]['round_index'] == 207
old_entries = copy.deepcopy(ledger['rounds'][:-1])
entry = ledger['rounds'][-1]
entry.update(status='closed', closing_assessment=assessment, completed_at=now, next_round=208)
for t in entry['tasks']:
    t['status'] = 'completed'
matches = list(re.finditer(r'    \{\r?\n      "round_index": 207,', s))
assert len(matches) == 1
pos = matches[0].start()
eol = '\r\n' if '\r\n' in s else '\n'
new = s[:pos] + eol.join('    ' + line for line in json.dumps(entry, indent=2, ensure_ascii=False).splitlines()) + eol + '  ]' + eol + '}' + eol
assert json.loads(new) == ledger and json.loads(new)['rounds'][:-1] == old_entries
assert new[:pos].encode('utf-8') == ledger_raw[:len(s[:pos].encode('utf-8'))]
lp.write_bytes(new.encode('utf-8'))

# Only after closing207: record a proposed direction, not a frozen/new round.
write('state/next_round_plan.yml', dict(
    round_index=208, status='pending_design', campaign_id=None,
    starting_graph_sha256=sha(gp), predecessor_round=207,
    predecessor_terminal_label=terminal, tasks=[],
    candidate_objective='Mandatory broad strategy and current-primary-literature review after205--207: '
                        'select a complete arithmetic objective capable of a genuine parent or exponent gain.',
    candidate_method='Compare signed rational total-frequency aggregation, actual high-value arithmetic, '
                     'and other full-source routes with current harmonic, spectral, geometric and arithmetic methods. '
                     'Audit exact theorem hypotheses and every reconstruction cost before selecting a route.',
    first_unproved_estimate='The full signed middle p12 target T^(29/25), or a sufficient K6 bound '
                            'T^(129/25-6omega). Existing bound leaves g=6omega-4/25-29alpha/110>0 everywhere.',
    exact_closed_dependencies=[p.as_posix() for p in evidence] + [judge.as_posix(), (base / 'synthesis.md').as_posix()],
    design_constraint='Design only after closed207 evidence. Repeating an auxiliary transform, recovered variance, '
                      'single-frequency grouping or termwise sextuple majorant is not a new gain. '
                      'Do not infer a target refutation from a scoped majorant obstruction.',
    full_goal_scope='Retain the full quarter theorem, adequate high-moment requirements and open M1/M2. '
                    'The current p12 milestone would only imply102/325.',
    scheduled_review='Round208 is the required broad strategy/current-literature checkpoint.',
    prior_turn_classification=assessment['goal_turn_classification'],
))
summary = _next_campaign(m, output_dir=base, graph_hash=sha(gp))
summary += ('\n## Closing decision\n\nRound207 closed with a scoped absolute-expansion no-go '
            'and a fully priced complete arithmetic attempt. Identity State Patch; all399 graph '
            'nodes and proof-draft bytes unchanged. The signed middle p12 target and full quarter '
            'theorem remain open. Round208 is pending design; broad review208.\n')
for p in ['state/current_round.md', 'state/next_campaign.md']:
    Path(p).write_text(summary, encoding='utf-8', newline='\n')
note = """
## Round207 signed rational-filter attack (2026-09-27)

The complete signed reciprocal estimate recovers the existing physical
coefficient supremum. Direct rational variance pays collisions, variable
width and moving prefixes with logarithms. The hyperbola threshold error
is target-safe; an independently reviewed even cutoff makes it rapid.

Actual single-frequency grouping leaves l1 mass of order sqrt(X).
The termwise integrated rational sixth majorant is at least X^3H,
exceeding the sufficient threshold by at least T^(517/250). This lower
bound includes exact and near triple relations and does not lower-bound
the signed moment or reject joint total-frequency cancellation.

Identity State Patch: all399 graph nodes and proof-draft bytes unchanged.
No improved complete moment or pointwise exponent; M1/M2 and quarter
remain open. Three reports and three exact-hash seams are green in their
declared scopes. See rounds/codex-managed/gc-signed-rational-filter-attack/synthesis.md.
Round208 is pending design as the mandatory broad strategy and current-
literature review after205--207.
"""
for p in ['state/project_summary.md', 'state/current_state.md', 'state/failure_ledger.md']:
    path = Path(p)
    raw = path.read_bytes()
    assert b'## Round207 signed rational-filter attack (2026-09-27)' not in raw
    path.write_bytes(raw + ('\n' + note).encode('utf-8'))

assert not subprocess.check_output(['git', 'diff', '--name-only', '--',
                                   'rounds/obligation-main', 'rounds/web-research-test']).strip()
assert all(sha(p) == h for p, h in start.items())
validation = dict(preflight, campaign_id=cid, generated_at=now,
                  terminal_label=terminal, starting_graph_sha256=start[gp.as_posix()],
                  final_graph_sha256=sha(gp),
                  canonical_graph_sha256=hashlib.sha256(dump_graph(g).encode()).hexdigest(),
                  graph_nodes=399, original_graph_raw_bytes_unchanged=True,
                  proof_draft_raw_bytes_unchanged=True, previous_ledger_prefix_bytes_unchanged=True,
                  legacy_paths_unchanged=True, next_strategy_checkpoint=208)
validation['status'] = 'green_round207_scoped_rational_closure_no_complete_bound_gain'
write(base / 'controls/closure_validation.json', validation)
vtext = (f'# Round207 closure validation\n\nGREEN for scoped rational-attempt closure only; '
         f'the signed target remains OPEN.\n\nGraph SHA256: `{sha(gp)}`. The identity patch was '
         'validated, applied in memory, reversed and replayed. All399 nodes, graph and proof-draft '
         'bytes and previous ledger prefix bytes are unchanged. Three seven-section reports, '
         'three final-hash reviews, conductor reconciliation, frozen inputs, Round200--206 '
         'archive hashes and output hygiene passed. No improved complete moment or pointwise '
         'exponent was promoted.\n\nSchema validation does not reprove historical nodes or remove '
         'inherited advisories. No mathematical numerical experiment occurred. '
         'Round208 is pending design; the next broad review is208.\n\n'
         f'Details: `{base.as_posix()}/controls/closure_validation.json`.\n')
for p in ['state/last_validation.md', 'state/last_validation_report.md']:
    Path(p).write_text(vtext, encoding='utf-8', newline='\n')
assert not validate_graph(load_graph(gp), root=root)
assert not validate_campaign(read('state/active_campaign.yml'), g, root=root)
subprocess.run(['git', 'diff', '--check'], check=True)
hashes = {p.relative_to(root).as_posix(): sha(p)
          for p in sorted((root / base).rglob('*'))
          if p.is_file() and p.name != 'artifact_hashes.json' and '__pycache__' not in p.parts}
strategy = Path('strategy/round207_signed_rational_filter_attack.md')
hashes[strategy.as_posix()] = sha(strategy)
write(base / 'controls/artifact_hashes.json', hashes)
print(json.dumps({k: validation[k] for k in [
    'status', 'graph_nodes', 'final_graph_sha256', 'proof_draft_raw_bytes_unchanged',
    'complete_moment_bound_improved', 'pointwise_exponent_change']}, indent=2))
