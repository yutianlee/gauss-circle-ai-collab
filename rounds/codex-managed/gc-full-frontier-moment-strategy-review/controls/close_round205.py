"""Close the scheduled strategy review with a byte-preserving identity patch."""
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

cid = 'gc-full-frontier-moment-strategy-review'
base = Path('rounds/codex-managed') / cid
terminal = 'strategy_review_select_complete_arithmetic_objective'
checkpoint = Path('strategy/gauss_circle_strategy_checkpoint_round205_2026-09-26.md')
now = datetime.now(timezone.utc).isoformat()

def read(p):
    return json.loads(Path(p).read_text(encoding='utf-8-sig'))

def write(p, obj):
    Path(p).write_text(json.dumps(obj, indent=2, ensure_ascii=False) + '\n',
                       encoding='utf-8', newline='\n')

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def contract(p):
    s = Path(p).read_text(encoding='utf-8')
    assert all(re.search(rf'^## {i}\.', s, re.M) for i in range(1, 8)), p
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
]
archive_count = 0
for prior in prior_campaigns:
    for p, h in read(Path('rounds/codex-managed') / prior / 'controls/artifact_hashes.json').items():
        assert sha(p) == h, ('Closed artifact changed', p)
        archive_count += 1

gp = Path('state/proof_obligations.yml')
oldraw = gp.read_bytes()
g = load_graph(gp)
assert len(g['proof_obligations']) == 399
assert not validate_graph(g, root=root)
m = read('state/active_campaign.yml')
assert m['round_index'] == 205 and m['campaign_id'] == cid and m['status'] == 'active'
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

reviews = [
    (base / 'reviews/independent_middle_band_review.md',
     base / 'controls/conductor_middle_band_strategy.md'),
    (base / 'reviews/independent_modular_cost_review.md',
     base / 'reports/internal_arithmetic_routes.md'),
    (base / 'reviews/independent_arithmetic_source_review.md',
     base / 'controls/conductor_arithmetic_source_gate.md'),
]
for review, artifact in reviews:
    s = contract(review)
    assert 'GREEN' in s and sha(artifact).lower() in s.lower(), review
judge = base / 'reviews/conductor_round205_reconciliation.md'
assert 'GREEN for strategy closure only' in contract(judge)
assert checkpoint.is_file() and (base / 'synthesis.md').is_file()
for t in m['tasks']:
    assert sha(t['report_path']) in judge.read_text(encoding='utf-8'), t['id']

hygiene = []
for p in list(base.rglob('*.md')) + [checkpoint]:
    s = p.read_text(encoding='utf-8')
    assert '\ufffd' not in s and not any(ord(c) < 32 and c not in '\n\r\t' for c in s), p
    hygiene.append(p.as_posix())
protected = [
    'GC-target', 'Conditional-bridge', 'M9', 'M9-M1', 'M9-M2',
    'M9-endpoint-uniformity', 'GC-external-Li-Yang-theta-star',
    'GC-weighted-square-root-exact-resonance-mass',
    'GC-physical-twelfth-moment-absolute-majorant-obstruction',
    'GC-complete-square-root-large-values-moment-bound',
]
reason = ('Scheduled full-frontier review completed. Exact modular completion and current '
          'theorem costs give no certified arithmetic gain. The complete middle-band signed '
          'shell moment is selected as the next proposed objective, with all other frequency '
          'ranges estimated at the milestone scale. No new graph theorem or exponent.')
patch = dict(
    round_index=205, campaign_id=cid, starting_graph_sha256=start[gp.as_posix()],
    proof_obligations=dict(create=[], update=[], correct_rejected=[], reject=[], no_change=protected),
    round_assessment=dict(terminal_label=terminal, reason=reason),
    reversibility=dict(rule='Identity patch. In-memory application, inverse identity and replay '
                       'equal the original graph; original graph and proof-draft bytes are not rewritten.'),
)
assert not validate_patch_against_graph(g, patch)
applied, result = apply_state_patch(copy.deepcopy(g), patch, round_index=205, judge_ref=judge.as_posix())
assert applied == g and not result.created and not result.updated
assert not result.rejected and not result.corrected_rejected
reversed_graph = copy.deepcopy(applied)
assert reversed_graph == g
replay, _ = apply_state_patch(copy.deepcopy(reversed_graph), patch, round_index=205, judge_ref=judge.as_posix())
assert replay == g and dump_graph(replay) == dump_graph(g)
write(base / 'state_patch.json', patch)
preflight = dict(
    round_index=205, status='green_identity_patch_preflight',
    graph_schema='pass', campaign_schema='pass', identity_patch='pass',
    all_399_nodes_and_other_graph_data_unchanged=True, reverse_identity_replay='pass',
    exact_review_hashes={a.as_posix(): sha(a) for _, a in reviews},
    three_report_hashes={t['report_path']: sha(t['report_path']) for t in m['tasks']},
    frozen_scope_and_briefs_unchanged=True, closed_round200_through204_archives_unchanged=True,
    protected_archive_entries_checked=archive_count,
    checkpoint_sha256=sha(checkpoint), report_hygiene=hygiene,
    mathematical_numerical_experiments=0, analytic_target='open', exponent_change=False,
)
write(base / 'controls/closure_preflight.json', preflight)
matrix = read('state/validation_matrix.yml')
for gate in matrix['gates']:
    if gate['id'].startswith('round205_'):
        gate['status'] = 'green_strategy_only_target_open'
for review, _ in reviews:
    matrix['gates'].append(dict(id='round205_' + review.stem, status='green', artifact=review.as_posix()))
matrix['gates'].append(dict(id='round205_identity_patch_scope', status='green',
                           artifact=(base / 'controls/closure_preflight.json').as_posix()))
assert all(x['status'].startswith('green') and Path(x['artifact']).is_file()
           for x in matrix['gates'] if x['id'].startswith('round205_'))
matrix.update(
    promotion_status='round_205_closed_identity_patch_strategy_adjusted', graph_sha256=sha(gp),
    analytic_target_status='open_complete_arithmetic_middle_band_moment',
    decision_rule='Round205 closes the mandatory full-frontier and primary-method review. '
                  'Identity State Patch; all mathematics and exponents unchanged. '
                  'Round206 pending design; next broad review208.',
)
write('state/validation_matrix.yml', matrix)
# All gates precede application to durable state. The validated mutation is identity.
assert gp.read_bytes() == oldraw and all(sha(p) == h for p, h in start.items())
assessment = dict(
    decision='retain_graph_select_complete_signed_shell_objective', terminal_label=terminal,
    graph_mutation=False, main_result=reason, resulting_graph_sha256=sha(gp),
    patch_effect=f'0_create_0_update_0_correct_0_reject_{len(protected)}_no_change',
    pointwise_exponent_change=False, new_mathematical_bound=False,
    strategy_checkpoint=checkpoint.as_posix(),
)
m.update(status='complete', completed_at=now, closing_assessment=assessment,
         post_report_reviews=[p.as_posix() for p, _ in reviews],
         conductor_interventions=[
             'Kept three primary theorem interfaces per harmonic task and two per modular task; conditional Baier record was metadata only.',
             'Reused completed tasks for one bounded same-round seam cycle; statement-only report finished before unmasking.',
             'Added explicit enlarged persistence window and harmless origin-count convention before final review hashes.',
             'Retained strategy lemmas as evidence rather than creating graph fragments; selected one complete arithmetic moment objective.',
         ])
for t in m['tasks']:
    t['status'] = 'completed'
assert not validate_campaign(m, g, root=root)
write('state/active_campaign.yml', m)

# Splice only the final ledger entry, preserving the earlier bytes exactly.
lp = Path('state/round_ledger.yml')
ledger_raw = lp.read_bytes()
s = ledger_raw.decode('utf-8')
ledger = json.loads(s)
assert ledger['active_round'] == 205 and ledger['rounds'][-1]['round_index'] == 205
old_entries = copy.deepcopy(ledger['rounds'][:-1])
entry = ledger['rounds'][-1]
entry.update(status='closed', closing_assessment=assessment, completed_at=now, next_round=206)
for t in entry['tasks']:
    t['status'] = 'completed'
match = list(re.finditer(r'    \{\r?\n      "round_index": 205,', s))
assert len(match) == 1
pos = match[0].start()
eol = '\r\n' if '\r\n' in s else '\n'
new = s[:pos] + eol.join('    ' + line for line in json.dumps(entry, indent=2, ensure_ascii=False).splitlines()) + eol + '  ]' + eol + '}' + eol
assert json.loads(new) == ledger and json.loads(new)['rounds'][:-1] == old_entries
assert new[:pos].encode('utf-8') == ledger_raw[:len(s[:pos].encode('utf-8'))]
lp.write_bytes(new.encode('utf-8'))

# Round205 is now closed; the following is a proposed direction, not a frozen successor.
write('state/next_round_plan.yml', dict(
    round_index=206, status='pending_design', campaign_id=None,
    starting_graph_sha256=sha(gp), predecessor_round=205,
    predecessor_terminal_label=terminal, tasks=[],
    candidate_objective='Prove or obtain a complete costed failure for the actual signed middle-band shell '
                        'twelfth moment M6 in the reviewed Round205 conductor interface: '
                        'T^(52/125)<N<T^(99/125), radius window [T/sqrt(2),sqrt(3)T], '
                        'target T^(29/25+epsilon). All complementary frequencies already have that moment bound.',
    candidate_method='Open r2=4 sum_(d|n)chi4(d) inside the exact odd shell filter; attempt a quantitative '
                     'signed shifted-correlation or spectral bound at squared-radius width '
                     'X^(151/500)<h<X^(99/250), retaining repeated shifts, local densities, curvature and all tails.',
    first_unproved_estimate='M6 itself, or a uniform target-sized single-block estimate throughout the entire middle range. '
                            'Required net moment saving:10beta-29/25.',
    design_constraint='Design only from closed205 artifacts. Do not repeat the transform, delete exceptional peaks, '
                      'assume unpriced tensor norms, or replace the complete band by smaller unestimated sectors.',
    full_goal_scope='If proved, p12 milestone gives only102/325. Quarter theorem still needs adequate arbitrarily '
                    'high fixed moments or stronger arithmetic information; fixed high-level cutoff alone cannot suffice.',
    scheduled_review='Mandatory next broad strategy/current-literature review208, after205--207.',
    prior_turn_classification='strategy_review_complete_no_new_mathematical_bound',
))
summary = _next_campaign(m, output_dir=base, graph_hash=sha(gp))
summary += ('\n## Closing decision\n\nRound205 completed the scheduled strategy review. '
            'Identity State Patch; all399 nodes, proof draft and exponents unchanged. '
            'The reviewed complete middle-band signed arithmetic moment is selected as the proposed206 objective. '
            'No new theorem or quarter proof. Round206 remains pending design; next broad review208.\n')
for p in ['state/current_round.md', 'state/next_campaign.md']:
    Path(p).write_text(summary, encoding='utf-8', newline='\n')
note = '''
## Round 205 strategy checkpoint (2026-09-26)

The mandatory full-frontier/current-literature review is complete. The
complete original-t=1 source now has an exact modular completion, but
the certified joint coefficient and outer-sum costs overwhelm the audited
scalar theorem savings. The current whole-discrepancy moment family cannot
self-bootstrap to a better pointwise exponent. New arithmetic-sensitive
correlation and random-model sources leave a thin-range or exceptional-set gap.

The selected proposed206 objective is the complete actual signed shell
twelfth moment over T^(52/125)<N<T^(99/125), with target T^(29/25+epsilon).
The reviewed outer-range argument pays the singleton, all complementary
frequencies and infinite tails. The middle moment remains unproved; its
success would imply only102/325, not the quarter theorem.

Round205 closed with an identity State Patch: all399 graph nodes and the
proof draft remain byte-for-byte unchanged. No new theorem or pointwise
exponent was promoted. See
`strategy/gauss_circle_strategy_checkpoint_round205_2026-09-26.md` and
`rounds/codex-managed/gc-full-frontier-moment-strategy-review/synthesis.md`.
Round206 is pending design; the next mandatory broad review is208.
'''
for p in ['state/project_summary.md', 'state/current_state.md', 'state/failure_ledger.md']:
    path = Path(p)
    old = path.read_text(encoding='utf-8')
    assert '## Round 205 strategy checkpoint (2026-09-26)' not in old
    path.write_text(old.rstrip() + '\n' + note, encoding='utf-8', newline='\n')

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
validation['status'] = 'green_round205_strategy_closure_no_new_bound'
write(base / 'controls/closure_validation.json', validation)
vtext = (f'# Round205 closure validation\n\nGREEN for strategy closure only; arithmetic target OPEN.\n\n'
         f'Graph SHA256: `{sha(gp)}`. The identity State Patch was validated, applied in memory, '
         'reversed and replayed with exact structural and canonical equality. Original graph and '
         'proof-draft bytes, all399 nodes, and previous ledger prefix bytes are unchanged. '
         'Three seven-section reports, three exact-hash seam reviews, conductor reconciliation, '
         'frozen inputs, Round200--204 archive hashes and file hygiene passed. '
         'No new mathematical bound or exponent is promoted.\n\n'
         'Graph-schema validation does not reprove historical nodes or remove inherited advisories. '
         'No mathematical numerical experiment occurred. Round206 is pending design; next broad review208.\n\n'
         f'Details: `{base.as_posix()}/controls/closure_validation.json`.\n')
for p in ['state/last_validation.md', 'state/last_validation_report.md']:
    Path(p).write_text(vtext, encoding='utf-8', newline='\n')
assert not validate_graph(load_graph(gp), root=root)
assert not validate_campaign(read('state/active_campaign.yml'), g, root=root)
subprocess.run(['git', 'diff', '--check'], check=True)
hashes = {p.relative_to(root).as_posix(): sha(p)
          for p in sorted((root / base).rglob('*'))
          if p.is_file() and p.name != 'artifact_hashes.json' and '__pycache__' not in p.parts}
for p in [Path('strategy/round205_full_frontier_strategy_review.md'), checkpoint]:
    hashes[p.as_posix()] = sha(p)
write(base / 'controls/artifact_hashes.json', hashes)
print(json.dumps({k: validation[k] for k in ['status', 'graph_nodes', 'final_graph_sha256',
                                           'proof_draft_raw_bytes_unchanged', 'exponent_change']}, indent=2))
