"""Validate the isolated exact-resonance promotion and close Round 201."""
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
    load_graph, dump_graph, write_graph, validate_graph,
    validate_patch_against_graph, apply_state_patch,
)

cid = 'gc-whole-discrepancy-twelfth-moment'
base = Path('rounds/codex-managed') / cid
kernel = Path('proofs/kernels/gc_weighted_square_root_exact_resonance_mass.md')
node_id = 'GC-weighted-square-root-exact-resonance-mass'
now = datetime.now(timezone.utc).isoformat()
terminal = 'whole_discrepancy_moment_reduction_open_offdiagonal'

def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))

def write_json(path, value):
    Path(path).write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

starting = read_json(base / 'controls/starting_state_hashes.json')
assert all(digest(p) == h for p, h in starting.items()), 'Protected input changed'
graph_path = Path('state/proof_obligations.yml')
old_raw = graph_path.read_bytes()
graph = load_graph(graph_path)
old_canonical_hash = hashlib.sha256(dump_graph(graph).encode()).hexdigest()
assert old_canonical_hash == '3073235ad5677b9066f1336ec9d958b0e93b92d99cfa7ebea1d823146c799099'
manifest = read_json('state/active_campaign.yml')
assert manifest['round_index'] == 201 and manifest['campaign_id'] == cid
assert manifest['status'] == 'active', 'Closure must not be applied twice'
assert not validate_graph(graph, root=root)
assert not validate_campaign(manifest, graph, root=root)

for task in manifest['tasks']:
    text = Path(task['report_path']).read_text(encoding='utf-8')
    assert all(re.search(rf'^## {i}\.', text, re.MULTILINE) for i in range(1, 8))
review_path = base / 'reviews/independent_resonance_kernel_review.md'
review = review_path.read_text(encoding='utf-8')
assert 'GREEN for the exact-resonance kernel' in review
assert digest(kernel) in review, 'Independent review must cover exact kernel bytes'
judge = base / 'reviews/conductor_round201_reconciliation.md'
assert 'GREEN for the exact-resonance kernel' in judge.read_text(encoding='utf-8')
assert (base / 'synthesis.md').is_file()

# Check UTF-8 and unintended control characters in the actual new research artifacts.
checked = []
for path in [kernel, *base.rglob('*.md')]:
    text = path.read_text(encoding='utf-8')
    assert '\ufffd' not in text, path
    assert not any(ord(c) < 32 and c not in '\n\t\r' for c in text), path
    assert not re.search(r'\\\s*\{\s*\nm squarefree', text), path
    checked.append(path.as_posix())

old_ids = {n['id'] for n in graph['proof_obligations']}
protected_ids = [
    'GC-target', 'Conditional-bridge', 'M9', 'M9-M1', 'M9-M2',
    'M9-endpoint-uniformity', 'GC-external-Li-Yang-theta-star',
    'GC-global-real-second-moment-density-one-quarter',
    'M9-M1-hard-top-t1-comparable-factor-exchange-sector',
]
assert set(protected_ids) <= old_ids and node_id not in old_ids
node = {
    'id': node_id, 'type': 'lemma', 'track': 'proof_infrastructure',
    'title': 'Uniform weighted exact square-root resonance mass and even constant coefficient',
    'status': 'proved_internal',
    'statement_tex': 'For fixed integer k>=2 and b_n>=0, set A_d=sum_(s>=1)b_(d s^2) for squarefree d and S=sum_d A_d^2<infinity. The sum over all 2^k sign vectors and ordered n_j>=1 with sum_j epsilon_j sqrt(n_j)=0 of product_j b_(n_j) is at most 2^k B_k S^(k/2), where B_k counts set partitions of k labels with no singleton. The mixed bound is 2^k B_k product_j S_j^(1/2). If b_n<=C tau(n)n^(-3/4), then S<=C^2 zeta(3/2)^10. Exact-resonance tails with max n_j>U are bounded by k2^k B_k S_>U^(1/2) S^((k-1)/2), tending uniformly to zero under a common divisor envelope. For real coefficients |a_n|<=b_n the even cosine exact coefficient is nonnegative; its contribution against w(R/T)>=0 is <=T||w||_1 B_k S^(k/2). Identification with the full infinite moment additionally requires sum|a_n|<infinity. For a_n(T)=r_2(n)n^(-3/4)Psi(sqrt(n/T)), real Schwartz Psi with |Psi|<=1, this yields 0<=D_12(T)<=T||w||_1 B_12 4^12 zeta(3/2)^60. Only zero radical differences are estimated: no finite-window near-resonance, full twelfth-moment, M1/M2 or pointwise exponent estimate follows.',
    'dependencies': ['H1-H3', 'Divisor-bound-elementary'],
    'implies': [], 'blockers': [],
    'evidence': {
        'positive': [kernel.as_posix(),
            (base / 'reports/blind_exact_resonance_rederivation.md').as_posix(),
            (base / 'reports/whole_moment_analytic_attack.md').as_posix(),
            (base / 'controls/conductor_resonance_and_bridge_analysis.md').as_posix(),
            review_path.as_posix(), judge.as_posix()],
        'negative': [], 'inconclusive': [],
    },
    'owner': 'Codex conductor',
    'next_action': 'Use only to remove the exact-frequency part of a complete fixed-window moment. The actual signed displaced nonzero-frequency aggregate remains unproved; no parent or exponent is discharged.',
}
patch = {
    'round_index': 201, 'campaign_id': cid,
    'starting_graph_sha256': starting[graph_path.as_posix()],
    'proof_obligations': {'create': [node], 'update': [], 'correct_rejected': [],
                           'reject': [], 'no_change': protected_ids},
    'round_assessment': {'terminal_label': terminal,
        'reason': 'Promote only the independently proved full weighted exact-resonance kernel. Complete fixed-window reduction and audited moment benchmark leave the actual signed offdiagonal estimate open; no pointwise exponent improvement.'},
    'reversibility': {'remove_created_ids': [node_id],
        'rule': 'Removing the sole created node restores all prior structured graph data and the original canonical hash. CRLF serialization restores the original raw byte hash. Replay from restored graph agrees except for the new-node timestamp; no old record may differ.'},
}
assert not validate_patch_against_graph(graph, patch)
applied, result = apply_state_patch(copy.deepcopy(graph), patch, round_index=201, judge_ref=judge.as_posix())
assert result.created == [node_id] and not result.updated and not result.rejected
assert not validate_graph(applied, root=root)
assert applied['proof_obligations'][:-1] == graph['proof_obligations']
assert all(applied[k] == graph[k] for k in graph if k != 'proof_obligations')
index = {n['id']: n for n in applied['proof_obligations']}
for dep in node['dependencies']:
    assert index[dep]['status'] in {'proved_internal', 'proved_external_dependency'}
for bucket in node['evidence'].values():
    assert all(Path(p).is_file() for p in bucket)

# A dependency walk for the newly introduced proof cone, not a claim about old cycles.
def walk(ident, active, visited):
    assert ident in index, ident
    assert ident not in active, ('cycle', ident)
    if ident in visited:
        return
    active.add(ident)
    for dep in index[ident].get('dependencies', []):
        walk(dep, active, visited)
    active.remove(ident)
    visited.add(ident)
walk(node_id, set(), set())
restored = copy.deepcopy(applied)
restored['proof_obligations'] = [n for n in restored['proof_obligations'] if n['id'] != node_id]
assert restored == graph
assert hashlib.sha256(dump_graph(restored).encode()).hexdigest() == old_canonical_hash
assert dump_graph(restored).replace('\n', '\r\n').encode() == old_raw
replayed, _ = apply_state_patch(copy.deepcopy(restored), patch, round_index=201, judge_ref=judge.as_posix())
replayed['proof_obligations'][-1]['last_updated_at'] = applied['proof_obligations'][-1]['last_updated_at']
assert replayed == applied
write_json(base / 'state_patch.json', patch)
preflight = {'status': 'green', 'round_index': 201,
    'graph_schema': 'pass', 'campaign_schema': 'pass', 'state_patch': 'pass',
    'new_dependency_cone': 'acyclic_with_accepted_dependencies',
    'all_396_existing_nodes_and_other_graph_data_unchanged': True,
    'reverse_structured_and_original_raw_hash': 'pass',
    'replay_except_new_timestamp': 'pass', 'exact_reviewed_kernel_sha256': digest(kernel),
    'artifact_utf8_and_control_checks': checked, 'analytic_target': 'open',
    'exponent_change': False}
write_json(base / 'controls/promotion_preflight.json', preflight)

# Finish every applicable promotion gate before changing the authoritative graph.
matrix = read_json('state/validation_matrix.yml')
for gate in matrix['gates']:
    if gate['id'].startswith('round201_'):
        gate['status'] = 'green_reviewed_stated_scope_offdiagonal_open'
matrix['gates'].extend([
    {'id': 'round201_independent_formal_kernel', 'status': 'green', 'artifact': review_path.as_posix()},
    {'id': 'round201_patch_reverse_replay_and_scope', 'status': 'green',
     'artifact': (base / 'controls/promotion_preflight.json').as_posix()},
])
assert all(g['status'].startswith('green') and Path(g['artifact']).is_file()
           for g in matrix['gates'] if g['id'].startswith('round201_'))
matrix['promotion_status'] = 'round_201_gates_green_exact_resonance_only_ready_to_apply'
matrix['analytic_target_status'] = 'open_signed_nonzero_frequency_twelfth_moment'
write_json('state/validation_matrix.yml', matrix)
write_graph(graph_path, applied)
assert load_graph(graph_path) == applied and not validate_graph(applied, root=root)
final_hash = digest(graph_path)
matrix['promotion_status'] = 'round_201_closed_one_exact_resonance_kernel_promoted_no_exponent_change'
matrix['graph_sha256'] = final_hash
write_json('state/validation_matrix.yml', matrix)

# Only now append the accepted kernel to the proof draft.
draft_path = Path('state/best_proof_draft.md')
assert digest(draft_path) == starting[draft_path.as_posix()]
draft = draft_path.read_text(encoding='utf-8')
draft_addition = '''
## Round 201 accepted weighted exact-resonance kernel

The accepted node `GC-weighted-square-root-exact-resonance-mass` proves
that, for b_n>=0, A_d=sum_s b_(d s^2) over squarefree d and S=sum_d A_d^2,
the full ordered k-root exact-resonance mass is at most 2^k B_k S^(k/2),
where B_k counts label partitions without singleton blocks. All signs,
nonpairings, unequal supports and infinite limits are included. For
b_n<=C tau(n)n^(-3/4), S<=C^2 zeta(3/2)^10. The mixed bound also gives
uniform exact-resonance tails under a common envelope.

For real cosine coefficients, the total even exact coefficient is a
nonnegative torus constant coefficient. The actual smoothed circle
coefficients have C=4, so their exact twelfth-moment contribution is
0<=D_12(T)<<T, uniformly in the smoothing scale. Individual exact terms
need not be positive. The kernel is proved in
`proofs/kernels/gc_weighted_square_root_exact_resonance_mass.md` and was
independently reviewed with statement-only rederivation and seam checks.

This controls only zero radical difference. The complete signed sum
over nonzero differences, with displaced Fourier weight retained,
remains unproved. No full twelfth-moment estimate, M1/M2 parent, endpoint
obligation, quarter theorem, or pointwise exponent is discharged.
'''
assert '## Round 201 accepted weighted exact-resonance kernel' not in draft
draft_path.write_text(draft.rstrip() + '\n' + draft_addition, encoding='utf-8')

assessment = {'decision': 'promote_exact_resonance_kernel_keep_full_moment_open',
    'terminal_label': terminal, 'graph_mutation': True,
    'main_result': patch['round_assessment']['reason'],
    'resulting_graph_sha256': final_hash,
    'patch_effect': f'1_create_0_update_0_correct_0_reject_{len(protected_ids)}_no_change',
    'exponent_change': False}
manifest['status'] = 'complete'
manifest['completed_at'] = now
manifest['closing_assessment'] = assessment
for task in manifest['tasks']:
    task['status'] = 'completed'
manifest['tasks'][0]['post_isolation_review_path'] = review_path.as_posix()
assert not validate_campaign(manifest, applied, root=root)
write_json('state/active_campaign.yml', manifest)

# Preserve the historical ledger text verbatim before its last entry.
ledger_path = Path('state/round_ledger.yml')
ledger_text = ledger_path.read_text(encoding='utf-8')
ledger = json.loads(ledger_text)
assert ledger['active_round'] == 201 and ledger['rounds'][-1]['round_index'] == 201
entry = ledger['rounds'][-1]
entry.update(status='closed', closing_assessment=assessment, completed_at=now, next_round=202)
for task in entry['tasks']:
    task['status'] = 'completed'
offset = ledger_text.rfind('    {\n      "round_index": 201,')
assert offset > 0
entry_text = '\n'.join('    ' + line for line in json.dumps(entry, indent=2, ensure_ascii=False).splitlines())
new_ledger = ledger_text[:offset] + entry_text + '\n  ]\n}\n'
assert json.loads(new_ledger) == ledger
ledger_path.write_text(new_ledger, encoding='utf-8')

summary = _next_campaign(manifest, output_dir=base, graph_hash=final_hash)
summary += ('\n## Closing decision\n\nOnly the exact-resonance kernel was promoted. '
            'The signed whole-discrepancy twelfth moment remains open; no exponent changed. '
            'Round 202 is pending design and must perform the scheduled strategy/current-literature checkpoint.\n')
for name in ['state/current_round.md', 'state/next_campaign.md']:
    Path(name).write_text(summary, encoding='utf-8')
write_json('state/next_round_plan.yml', {
    'round_index': 202, 'status': 'pending_design', 'campaign_id': None,
    'starting_graph_sha256': final_hash, 'predecessor_round': 201,
    'predecessor_terminal_label': terminal, 'tasks': [],
    'scheduled_review': 'Mandatory global strategy and current-primary-literature checkpoint after Rounds 199--201.',
    'inherited_frontier': 'Round 200 complete t=1 actual-vector even-Fejer correlation remains open. Round 201 complete whole-discrepancy moment reduction has uniform exact part O(T); the signed nonzero-frequency twelfth-moment estimate remains open. Verified published q<=262/27 interpolation leaves Y-exponent gap (185-578theta_LY)/54=0.059791190499861... before strict improvement.',
    'design_constraint': 'Review the full proof strategy and current primary methods before selecting one complete signed analytic target. Do not promote exact diagonal bounds, representation changes, or P2 mechanism exclusions as full moment or exponent progress. Audit all source hypotheses and reconstruction losses.',
    'proof_state_effect': 'none_until_new_round_is_designed_frozen_and_reviewed',
})
note = '''
## Round 201 whole-discrepancy moment boundary (2026-09-23)

The full fixed-window Poisson--Bessel expansion, smoothing errors,
uniform tails, and all-sign twelfth-moment identity are reviewed.
One internal weighted exact-resonance kernel is promoted, including
nonpairing relations and uniform exact tails. Its actual even exact
contribution is O(T); the signed nonzero-frequency estimate remains
open. The printed q<=262/27 absolute-moment benchmark with the accepted
pointwise theta gives eta=0.148072478162659..., above the improvement
threshold 0.088281287662798.... No existing obligation or exponent
changed. See `rounds/codex-managed/gc-whole-discrepancy-twelfth-moment/synthesis.md`.
Round 202 is pending design and begins with the scheduled strategy and
current-primary-literature checkpoint.
'''
for name in ['state/project_summary.md', 'state/current_state.md']:
    p = Path(name)
    old = p.read_text(encoding='utf-8')
    assert '## Round 201 whole-discrepancy moment boundary' not in old
    p.write_text(old.rstrip() + '\n' + note, encoding='utf-8')

assert digest('strategy/gauss_circle_strategy_review_2026-09-23.md') == starting['strategy/gauss_circle_strategy_review_2026-09-23.md']
legacy_paths = ['rounds/obligation-main', 'rounds/web-research-test',
                'rounds/codex-managed/m9-m1-t1-p2-cross-gcd-cellular-boundary-gate']
assert not subprocess.check_output(['git', 'diff', '--name-only', '--', *legacy_paths]).strip()
validation = dict(preflight, status='green_exact_kernel_promotion_and_round_closure',
    campaign_id=cid, generated_at=now, terminal_label=terminal,
    starting_graph_raw_sha256=starting[graph_path.as_posix()],
    starting_graph_canonical_sha256=old_canonical_hash,
    final_graph_sha256=final_hash, graph_nodes=len(applied['proof_obligations']),
    new_nodes=[node_id], accepted_proof_draft_updated_after_valid_patch=True,
    final_proof_draft_sha256=digest(draft_path),
    all_three_reports_and_independent_review_complete=True,
    legacy_and_round199_paths_unchanged=True, mathematical_numerical_experiments=0)
write_json(base / 'controls/closure_validation.json', validation)
validation_text = (f'# Round 201 closure validation\n\nClosed round: 201. Next round: 202 (pending design; mandatory strategy/literature review).\n\n'
    f'Campaign: `{cid}`. Terminal: `{terminal}`.\n\n'
    f'GREEN for isolated kernel promotion; full moment and pointwise improvement OPEN. Graph SHA-256: `{final_hash}`.\n\n'
    'One exact-resonance node was added; all 396 prior nodes and all other structured graph data are identical. '
    'Schema, evidence, accepted dependency cone, independent exact-hash review, reversal to original bytes, '
    'and replay excluding only the new timestamp passed. Applicable matrix gates were green before graph mutation. '
    'The proof draft was appended only after the graph patch was validated and applied. '
    'No numerical experiments or exponent change. Legacy evidence is unchanged.\n\n'
    f'Exact validation: `{base.as_posix()}/controls/closure_validation.json`.\n')
for name in ['state/last_validation.md', 'state/last_validation_report.md']:
    Path(name).write_text(validation_text, encoding='utf-8')
assert not validate_graph(load_graph(graph_path), root=root)
assert not validate_campaign(read_json('state/active_campaign.yml'), applied, root=root)
subprocess.run(['git', 'diff', '--check'], check=True)
artifact_hashes = {p.relative_to(root).as_posix(): digest(p) for p in sorted((root / base).rglob('*'))
                   if p.is_file() and p.name != 'artifact_hashes.json' and '__pycache__' not in p.parts}
artifact_hashes[kernel.as_posix()] = digest(kernel)
write_json(base / 'controls/artifact_hashes.json', artifact_hashes)
print(json.dumps({k:validation[k] for k in ['status','graph_nodes','new_nodes','final_graph_sha256','exponent_change']}, indent=2))
