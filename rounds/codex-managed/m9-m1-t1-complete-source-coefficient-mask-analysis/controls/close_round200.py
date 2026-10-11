"""Validate and record the Round-200 identity State Patch and workflow closure."""
from __future__ import annotations

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
    load_graph, validate_graph, validate_patch_against_graph, apply_state_patch,
)

cid = 'm9-m1-t1-complete-source-coefficient-mask-analysis'
base = Path('rounds/codex-managed') / cid
now = datetime.now(timezone.utc).isoformat()


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def write_json(path, value):
    Path(path).write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


starting = read_json(base / 'controls/starting_state_hashes.json')
assert all(digest(p) == h for p, h in starting.items()), 'Protected input changed'
graph = load_graph(Path('state/proof_obligations.yml'))
manifest = read_json('state/active_campaign.yml')
assert manifest['round_index'] == 200 and manifest['campaign_id'] == cid
assert manifest['status'] == 'active', 'This closure is not a repeatable overwrite'
issues = validate_graph(graph, root=root) + validate_campaign(manifest, graph, root=root)
assert not issues, issues

for task in manifest['tasks']:
    report = Path(task['report_path'])
    text = report.read_text(encoding='utf-8')
    assert all(re.search(rf'^## {i}\.', text, re.MULTILINE) for i in range(1, 8)), report

required = [
    'reviews/independent_operator_review.md',
    'reviews/conductor_report_reconciliation.md',
    'controls/conductor_complete_source_operator_analysis.md',
    'controls/conductor_launch_validation.md',
    'controls/round200_interventions.md',
    'synthesis.md',
]
assert all((base / p).is_file() for p in required)
assert 'GREEN after repair' in (base / required[0]).read_text(encoding='utf-8')
assert '(1-j/M)_+' in (base / required[2]).read_text(encoding='utf-8')

protected_ids = [
    'GC-target', 'Conditional-bridge', 'M9', 'M9-M1', 'M9-M2',
    'M9-M1-top-endpoint-signed-cone',
    'M9-M1-direct-smooth-residual-blockwise-estimate',
    'M9-M1-hard-top-high-radical-small-t-residual-estimate',
    'M9-M1-hard-top-t1-comparable-factor-exchange-sector',
    'M9-M1-hard-top-t1-residual-fejer-tangent-gcd-reduction',
    'M9-M1-hard-top-t1-rho-large-P2-absolute-capacity-sectors',
    'M9-M1-hard-top-t1-rho-large-P2-common-cell-allocation-commutator-sector',
    'M9-endpoint-uniformity',
]
ids = {n['id'] for n in graph['proof_obligations']}
assert set(protected_ids) <= ids
patch = {
    'round_index': 200,
    'campaign_id': cid,
    'starting_graph_sha256': starting['state/proof_obligations.yml'],
    'proof_obligations': {
        'create': [], 'update': [], 'correct_rejected': [], 'reject': [],
        'no_change': protected_ids,
    },
    'round_assessment': {
        'terminal_label': 'complete_source_interface_with_open_estimate',
        'reason': 'Complete-source coefficient, mask, and power analysis finished; the actual-vector L^2 correlation bound is unproved. No new parent estimate or exponent. Finite tools are archived without promotion.',
    },
    'reversibility': {
        'rule': 'Identity patch. In-memory application and replay equal the original graph; reversal is the identity. Do not serialize an unchanged graph merely to change its line endings.',
    },
}
assert not validate_patch_against_graph(graph, patch)
applied, result = apply_state_patch(copy.deepcopy(graph), patch, round_index=200,
                                    judge_ref=(base / 'reviews/conductor_report_reconciliation.md').as_posix())
assert applied == graph
assert not validate_graph(applied, root=root)
replayed, _ = apply_state_patch(copy.deepcopy(applied), patch, round_index=200)
assert replayed == graph
write_json(base / 'state_patch.json', patch)

legacy_paths = ['rounds/obligation-main', 'rounds/web-research-test',
                'rounds/codex-managed/m9-m1-t1-p2-cross-gcd-cellular-boundary-gate']
assert not subprocess.check_output(['git', 'diff', '--name-only', '--', *legacy_paths]).strip()
subprocess.run(['git', 'diff', '--check'], check=True)

terminal = patch['round_assessment']['terminal_label']
assessment = dict(decision='archive_complete_source_interface_keep_analytic_target_open',
                  terminal_label=terminal, graph_mutation=False,
                  main_result=patch['round_assessment']['reason'],
                  resulting_graph_sha256=starting['state/proof_obligations.yml'],
                  patch_effect=f'0_create_0_update_0_correct_0_reject_{len(protected_ids)}_no_change',
                  exponent_change=False)
manifest['status'] = 'complete'
manifest['completed_at'] = now
manifest['closing_assessment'] = assessment
for task in manifest['tasks']:
    task['status'] = 'completed'
manifest['tasks'][2]['post_isolation_review_path'] = (base / 'reviews/independent_operator_review.md').as_posix()
assert not validate_campaign(manifest, graph, root=root)
write_json('state/active_campaign.yml', manifest)

ledger_path = Path('state/round_ledger.yml')
ledger_text = ledger_path.read_text(encoding='utf-8')
ledger = json.loads(ledger_text)
assert ledger['active_round'] == 200 and ledger['rounds'][-1]['round_index'] == 200
entry = ledger['rounds'][-1]
entry['status'] = 'closed'
for task in entry['tasks']:
    task['status'] = 'completed'
entry['closing_assessment'] = assessment
entry['completed_at'] = now
entry['next_round'] = 201
marker = '    {\n      "round_index": 200,'
offset = ledger_text.rfind(marker)
assert offset > 0
entry_text = '\n'.join('    ' + line for line in json.dumps(entry, indent=2, ensure_ascii=False).splitlines())
new_ledger = ledger_text[:offset] + entry_text + '\n  ]\n}\n'
assert json.loads(new_ledger) == ledger
ledger_path.write_text(new_ledger, encoding='utf-8')

summary = _next_campaign(manifest, output_dir=base, graph_hash=starting['state/proof_obligations.yml'])
summary += f'\n## Closing decision\n\nTerminal label: `{terminal}`.\n\n'
summary += ('The complete-source interface is recorded; the actual-vector correlation estimate remains open. '
            'No graph or accepted proof-draft change, theorem promotion, or exponent improvement. '
            f'See `{base.as_posix()}/synthesis.md`. Round 201 is pending design.\n')
Path('state/current_round.md').write_text(summary, encoding='utf-8')
Path('state/next_campaign.md').write_text(summary, encoding='utf-8')
write_json('state/next_round_plan.yml', {
    'round_index': 201, 'status': 'pending_design', 'campaign_id': None,
    'starting_graph_sha256': starting['state/proof_obligations.yml'],
    'predecessor_round': 200, 'predecessor_terminal_label': terminal,
    'inherited_frontier': 'Complete original-t=1 residual actual-vector even-Fejer estimate Q_R << L^2 X^epsilon remains open. Complete endpoint/product coefficients have affordable rank-one norm; the universal coarse kernel costs L.',
    'design_constraint': 'Select one complete-source inequality using the closed Round-200 source/norm ledger. A Campaign-B import needs an exact arithmetic kernel and fully priced norms first. The auxiliary pre-selector scalar route separately requires a full literal V_g certificate and phase estimate B_g. Campaign C is independent. Do not return to counting P2 mechanism failures as exponent progress.',
    'proof_state_effect': 'none_until_new_round_is_designed_frozen_and_reviewed',
    'tasks': [],
    'scheduled_review': 'Round 202 remains the broad full-proof strategy and current-primary-literature checkpoint.',
})

matrix = read_json('state/validation_matrix.yml')
matrix['promotion_status'] = 'round_200_closed_complete_source_analysis_no_theorem_or_exponent_promotion'
matrix['analytic_target_status'] = 'open_complete_actual_vector_correlation'
for gate in matrix['gates']:
    if gate['id'].startswith('round200_'):
        gate['status'] = 'green_reviewed_interface_only_no_analytic_promotion'
matrix['gates'].append(dict(id='round200_identity_patch_and_protected_scope', status='green',
                            artifact=(base / 'controls/closure_validation.json').as_posix()))
write_json('state/validation_matrix.yml', matrix)

note = ('\n## Round 200 complete-source analysis (2026-09-23)\n\n'
        'The requested strategy review redirected work to the complete original-t=1 residual before '
        'P1/P2 norms. Its actual product-coordinate coefficient norm is affordable, but the generic '
        'even-Fejer operator still costs L. The complete actual-vector L^2 correlation bound remains open. '
        'The conditional mask/norm and scalar alternatives are recorded in '
        '`rounds/codex-managed/m9-m1-t1-complete-source-coefficient-mask-analysis/synthesis.md`. '
        'Round 200 closes as analysis with an identity State Patch: no theorem or exponent improvement, '
        'no change to accepted graph or proof draft. Round 201 is pending design.\n')
for name in ['state/project_summary.md', 'state/current_state.md']:
    p = Path(name)
    old = p.read_text(encoding='utf-8')
    assert '## Round 200 complete-source analysis' not in old
    p.write_text(old.rstrip() + '\n' + note, encoding='utf-8')

assert all(digest(p) == h for p, h in starting.items())
assert not validate_graph(load_graph(Path('state/proof_obligations.yml')), root=root)
assert not validate_campaign(read_json('state/active_campaign.yml'), graph, root=root)
validation = {
    'round_index': 200, 'campaign_id': cid, 'generated_at': now,
    'terminal_label': terminal, 'status': 'green_analysis_closure',
    'graph_validation': 'pass', 'campaign_validation': 'pass',
    'identity_state_patch_validation': 'pass',
    'in_memory_application_equals_start': True, 'reverse_identity_and_replay_equals_start': True,
    'protected_input_hashes_unchanged': starting,
    'graph_nodes': len(graph['proof_obligations']), 'mathematical_numerical_experiments': 0,
    'three_seven_section_reports': 'present', 'independent_operator_review': 'green_after_repair',
    'legacy_and_round199_paths_unchanged': True,
    'accepted_proof_draft_updated': False, 'analytic_target': 'open', 'exponent_change': False,
}
write_json(base / 'controls/closure_validation.json', validation)
artifact_hashes = {p.relative_to(root).as_posix(): digest(p) for p in sorted((root / base).rglob('*'))
                   if p.is_file() and p.name != 'artifact_hashes.json' and '__pycache__' not in p.parts}
write_json(base / 'controls/artifact_hashes.json', artifact_hashes)

validation_text = (f'# Round 200 closure validation\n\nClosed round: 200. Next round: 201 (pending design).\n\n'
                   f'Campaign: `{cid}`. Terminal label: `{terminal}`.\n\n'
                   'Status: GREEN for analysis closure; complete arithmetic estimate OPEN.\n\n'
                   f'Raw graph SHA-256: `{starting["state/proof_obligations.yml"]}`.\n\n'
                   'Graph/campaign validation and the identity State Patch passed. In-memory application, '
                   'identity reversal and replay leave the complete graph equal to its starting state. '
                   'The graph and accepted proof draft retain their original byte hashes. Three reports, '
                   'independent finite derivation, repaired operator review, conductor reconciliation and '
                   'synthesis are complete. Legacy and Round-199 paths are unchanged.\n\n'
                   'No new parent estimate or exponent is proved. The remaining full-source correlation '
                   'loss is L; after scalar reconstruction it is L^(1/2). No external theorem was imported '
                   'and no numerical experiment was used.\n\n'
                   f'Exact validation: `{base.as_posix()}/controls/closure_validation.json`.\n')
Path('state/last_validation.md').write_text(validation_text, encoding='utf-8')
Path('state/last_validation_report.md').write_text(validation_text, encoding='utf-8')
subprocess.run(['git', 'diff', '--check'], check=True)
print(json.dumps(validation, indent=2))
