"""Record a verified resume; does not alter mathematical state or frozen scope."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

base = Path('rounds/codex-managed/gc-complete-large-values-duality')
def read(p):
    return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p, data):
    Path(p).write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

for control in ['starting_state_hashes.json', 'frozen_artifact_hashes.json']:
    for p, h in read(base/'controls'/control).items():
        assert sha(p) == h, p
checkpoint = read(base/'controls/paused_checkpoint.json')
kernel = 'proofs/kernels/gc_complete_square_root_large_values_moment_bound.md'
for p, h in checkpoint['artifact_sha256'].items():
    if p != kernel:
        assert sha(p) == h, p
assert sha(kernel) == '942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212'
manifest = read('state/active_campaign.yml')
assert manifest['round_index'] == 204 and manifest['status'] == 'active'
for task in manifest['tasks']:
    assert Path(task['report_path']).is_file()
    task['status'] = 'completed'
manifest['resume_record'] = {
    'resumed_at': datetime.now(timezone.utc).isoformat(),
    'goal_status_verified': 'active',
    'prior_goal_turn_classification': 'progress_completed_three_reports_candidate_not_yet_accepted',
    'pause_checkpoint': str(base/'controls/paused_checkpoint.json').replace('\\', '/'),
    'remaining_round_work': 'Exact-hash seam reviews, conductor reconciliation, validated State Patch and closure.',
}
manifest['conductor_interventions'] = [checkpoint['intervention'], {
    'task_id': 'gram_tail_seam_review',
    'change': 'Repair candidate Section5 by explicitly retaining singleton n=1.',
    'frozen_objective_changed': False,
    'old_candidate_sha256': checkpoint['artifact_sha256'][kernel],
    'new_candidate_sha256': sha(kernel),
}]
manifest['post_report_review_assignments'] = [
    {'id': 'gram_tail_seam_review', 'seam': 'Finite Gram, real covering, singleton, partial blocks and all tails'},
    {'id': 'source_correlation_seam_review', 'seam': 'Exact global source specialization and complete correlation ranges'},
    {'id': 'sharp_moment_seam_review', 'seam': 'Sharp reconstruction, all fixed moments and implication scope'},
]
write('state/active_campaign.yml', manifest)
write(base/'controls/resume_validation.json', {
    **manifest['resume_record'],
    'starting_state_and_frozen_artifacts': 'unchanged',
    'completed_report_hashes': {p: h for p, h in checkpoint['artifact_sha256'].items() if '/reports/' in p},
    'candidate_repair': manifest['conductor_interventions'][-1],
    'graph_mutated': False,
    'proof_draft_mutated': False,
    'numerical_experiments': 0,
})
print('Round204 resume verified; three reports preserved, candidate review active, graph unchanged.')
